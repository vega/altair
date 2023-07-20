import embed from "vega-embed";

export async function render({ model, el }) {
    let finalize;

    const reembed = async () => {
        if (finalize != null) {
          finalize();
        }

        let spec = model.get("spec");
        let api = await embed(el, spec);
        finalize = api.finalize;

        const selectionWatches = model.get("_selection_watches");
        const initialSelections = {};
        for (const selectionName of selectionWatches) {
            api.view.addSignalListener(selectionName, (_, value) => {
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
            api.view.addSignalListener(paramName, (_, value) => {
                const newParams = JSON.parse(JSON.stringify(model.get("_params"))) || {};
                newParams[paramName] = {value};
                model.set("_params", newParams);
                model.save_changes();
            });
            initialParams[paramName] = {value: api.view.signal(paramName)}
        }
        model.set("_params", initialParams);

        model.save_changes();
    }

    model.on('change:spec', reembed);
    await reembed();
}
