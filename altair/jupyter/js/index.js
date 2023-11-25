import embed from "https://esm.sh/vega-embed@6?deps=vega@5&deps=vega-lite@5.16.3";
import debounce from "https://esm.sh/lodash-es@4.17.21/debounce";

export async function render({ model, el }) {
    let finalize;

    function showError(error){
        el.innerHTML = (
            '<div style="color:red;">'
            + '<p>JavaScript Error: ' + error.message + '</p>'
            + "<p>This usually means there's a typo in your chart specification. "
            + "See the javascript console for the full traceback.</p>"
            + '</div>'
        );
    }

    const reembed = async () => {
        if (finalize != null) {
          finalize();
        }

        let spec = model.get("spec");
        let api;
        try {
            api = await embed(el, spec);
        } catch (error) {
            showError(error)
            return;
        }

        finalize = api.finalize;

        // Debounce config
        const wait = model.get("debounce_wait") ?? 10;
        const maxWait = wait;

        const initialSelections = {};
        for (const selectionName of Object.keys(model.get("_vl_selections"))) {
            const storeName = `${selectionName}_store`;
            const selectionHandler = (_, value) => {
                const newSelections = cleanJson(model.get("_vl_selections") ?? {});
                const store = cleanJson(api.view.data(storeName) ?? []);

                newSelections[selectionName] = {value, store};
                model.set("_vl_selections", newSelections);
                model.save_changes();
            };
            api.view.addSignalListener(selectionName, debounce(selectionHandler, wait, {maxWait}));

            initialSelections[selectionName] = {
                value: cleanJson(api.view.signal(selectionName) ?? {}),
                store: cleanJson(api.view.data(storeName) ?? [])
            }
        }
        model.set("_vl_selections", initialSelections);

        const initialParams = {};
        for (const paramName of Object.keys(model.get("_params"))) {
            const paramHandler = (_, value) => {
                const newParams = JSON.parse(JSON.stringify(model.get("_params"))) || {};
                newParams[paramName] = value;
                model.set("_params", newParams);
                model.save_changes();
            };
            api.view.addSignalListener(paramName, debounce(paramHandler, wait, {maxWait}));

            initialParams[paramName] = api.view.signal(paramName) ?? null
        }
        model.set("_params", initialParams);
        model.save_changes();

        // Param change callback
        model.on('change:_params', async (new_params) => {
            for (const [param, value] of Object.entries(new_params.changed._params)) {
                api.view.signal(param, value);
            }
            await api.view.runAsync();
        });
    }

    model.on('change:spec', reembed);
    model.on('change:debounce_wait', reembed);
    await reembed();
}

function cleanJson(data) {
    return JSON.parse(JSON.stringify(data))
}