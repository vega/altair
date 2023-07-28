import embed from "https://cdn.jsdelivr.net/npm/vega-embed@6/+esm";
import debounce from 'https://cdn.jsdelivr.net/npm/just-debounce-it@3.2.0/+esm'

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
            api.view.addSignalListener(selectionName, debounce(selectionHandler, wait, true));

            initialSelections[selectionName] = {value: {}, store: []}
        }
        model.set("_selections", initialSelections);

        const initialParams = {};
        for (const paramName of Object.keys(model.get("_params"))) {
            const paramHandler = (_, value) => {
                const newParams = JSON.parse(JSON.stringify(model.get("_params"))) || {};
                newParams[paramName] = value;
                model.set("_params", newParams);
                model.save_changes();
            };
            api.view.addSignalListener(paramName, debounce(paramHandler, wait, true));

            initialParams[paramName] = api.view.signal(paramName) ?? null
        }
        model.set("_params", initialParams);
        model.save_changes();

        // Param change callback
        model.on('change:_params', (new_params) => {
            for (const [param, value] of Object.entries(new_params.changed._params)) {
                api.view.signal(param, value);
            }
            api.view.run();
        });
    }

    model.on('change:spec', reembed);
    model.on('change:debounce_wait', reembed);
    await reembed();
}
