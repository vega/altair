import embed from "vega-embed";
import {debounce} from "lodash"

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
            const selectionHandler = (_, value) => {
                const newSelections = JSON.parse(JSON.stringify(model.get("_selections"))) || {};
                const store = JSON.parse(JSON.stringify(api.view.data(`${selectionName}_store`)));

                newSelections[selectionName] = {value, store};
                model.set("_selections", newSelections);
                model.save_changes();
            };
            api.view.addSignalListener(selectionName, debounce(selectionHandler, wait, {maxWait}));

            initialSelections[selectionName] = {value: {}, store: []}
        }
        model.set("_selections", initialSelections);

        const paramWatches = model.get("_param_watches");
        const initialParams = {};
        for (const paramName of paramWatches) {
            const paramHandler = (_, value) => {
                const newParams = JSON.parse(JSON.stringify(model.get("_params"))) || {};
                newParams[paramName] = {value};
                model.set("_params", newParams);
                model.save_changes();
            };
            api.view.addSignalListener(paramName, debounce(paramHandler, wait, {maxWait}));

            initialParams[paramName] = {value: api.view.signal(paramName) ?? null}
        }
        model.set("_params", initialParams);

        model.save_changes();

        // Register custom message handler
        model.on("msg:custom", msg => {
            if (msg.type === "setParams") {
                for (const update of msg.updates) {
                    api.view.signal(update.name, update.value);
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
