import embed from "vega-embed";
import {debounce, cloneDeep} from "lodash"

export async function render({ model, el }) {
    let finalize;

    const reembed = async () => {
        if (finalize != null) {
          finalize();
        }

        let spec = model.get("spec");
        let api = await embed(el, spec);
        finalize = api.finalize;

        // Debounce config
        const wait = model.get("debounce_wait") ?? 10;
        const maxWait = wait;

        const selectionWatches = model.get("_selection_watches");
        const initialSelections = {};
        for (const selectionName of selectionWatches) {
            // Selections assumed to be top-level (scope []) for now
            addSignalListener(api.view, selectionName, [], wait, maxWait, (_, value) => {
                const newSelections = JSON.parse(JSON.stringify(model.get("_selections"))) || {};
                const store = JSON.parse(JSON.stringify(api.view.data(`${selectionName}_store`)));

                newSelections[selectionName] = {value, store};
                model.set("_selections", newSelections);
                model.save_changes();
            });

            initialSelections[selectionName] = {value: {}, store: []}
        }
        model.set("_selections", initialSelections);

        const paramWatches = model.get("_param_watches");
        const initialParams = {};
        for (const paramName of paramWatches) {
            // Params assumed to be top-level (scope []) for now
            addSignalListener(api.view, paramName, [], wait, maxWait, (_, value) => {
                const newParams = JSON.parse(JSON.stringify(model.get("_params"))) || {};
                newParams[paramName] = {value};
                model.set("_params", newParams);
                model.save_changes();
            });

            initialParams[paramName] = {value: api.view.signal(paramName)}
        }
        model.set("_params", initialParams);

        model.save_changes();

        // Register custom message handler
        model.on("msg:custom", msg => {
            if (msg.type === "update") {
                console.log(msg);
                for (const update of msg.updates) {
                    if (update.namespace === "signal") {
                        setSignalValue(api.view, update.name, update.scope ?? [], update.value);
                    } else if (update.namespace === "data") {
                        setDataValue(api.view, update.name, update.scope ?? [], update.value);
                    }
                }
                api.view.run();
            } else {
                console.log(`Unexpected message type ${msg.type}`)
            }
        });
    }

    model.on('change:spec', reembed);
    model.on('change:debounce_wait', reembed);
    await reembed();
}


// Scoped data/signal utilities copied from vegafusion-wasm
function getNestedRuntime(view, scope) {
    // name is an array that may have leading integer group indices
    let runtime = view._runtime;
    for (const index of scope) {
        runtime = runtime.subcontext[index];
    }
    return runtime
}

function lookupSignalOp(view, name, scope) {
    // name is an array that may have leading integer group indices
    let parent_runtime = getNestedRuntime(view, scope);
    return parent_runtime.signals[name];
}

function dataref(view, name, scope) {
    // name is an array that may have leading integer group indices
    let parent_runtime = getNestedRuntime(view, scope);
    return parent_runtime.data[name];
}

export function getSignalValue(view, name, scope) {
    let signal_op = lookupSignalOp(view, name, scope);
    return cloneDeep(signal_op.value)
}

export function setSignalValue(view, name, scope, value) {
    let signal_op = lookupSignalOp(view, name, scope);
    view.update(signal_op, value);
}

export function getDataValue(view, name, scope) {
    let data_op = dataref(view, name, scope);
    return cloneDeep(data_op.values.value)
}

export function setDataValue(view, name, scope, value) {
    let dataset = dataref(view, name, scope);
    let changeset = view.changeset().remove(truthy).insert(value)
    dataset.modified = true;
    view.pulse(dataset.input, changeset);
}

export function addSignalListener(view, name, scope, wait, maxWait, handler) {
    let signal_op = lookupSignalOp(view, name, scope);
    let options = {};
    if (maxWait) {
        options["maxWait"] = maxWait;
    }

    return addOperatorListener(
        view,
        name,
        signal_op,
        debounce(handler, wait, options),
    );
}

export function addDataListener(view, name, scope, wait, maxWait, handler) {
    let dataset = dataref(view, name, scope).values;
    let options = {};
    if (maxWait) {
        options["maxWait"] = maxWait;
    }
    return addOperatorListener(
        view,
        name,
        dataset,
        debounce(handler, wait, options),
    );
}

// Private helpers from Vega
function findOperatorHandler(op, handler) {
    const h = (op._targets || [])
        .filter(op => op._update && op._update.handler === handler);
    return h.length ? h[0] : null;
}

function addOperatorListener(view, name, op, handler) {
    let h = findOperatorHandler(op, handler);
    if (!h) {
        h = trap(view, () => handler(name, op.value));
        h.handler = handler;
        view.on(op, null, h);
    }
    return view;
}

function trap(view, fn) {
    return !fn ? null : function() {
        try {
            fn.apply(this, arguments);
        } catch (error) {
            view.error(error);
        }
    };
}
