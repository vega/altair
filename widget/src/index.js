import embed from "vega-embed";

export async function render({ model, el }) {
    let spec = JSON.parse(model.get("spec"));
    let api = await embed(el, spec);
    api.view.addSignalListener(spec.params[0].name, (_, update) => {
        console.log(update);
        model.set("selection", update);
        model.save_changes();
    });
}
