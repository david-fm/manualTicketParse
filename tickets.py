import marimo

__generated_with = "0.2.2"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        """
        # Ticket Manual Parse

        Write the ticket id and the number of items in the ticket.
        """
    )
    return


@app.cell
def __(mo):
    ticket_id = mo.ui.text(label="Ticket id").form()
    ticket_id
    return ticket_id,


@app.cell
def __(__file__, mo, ticket_id):
    import os
    PATH = os.path.join(os.path.dirname(__file__),"Tickets",f"{ticket_id.value}.jpg")
    ticket_image = mo.image(src=PATH)
    return PATH, os, ticket_image


@app.cell
def __(mo):
    n_items = mo.ui.text(value="1", label="Number of items").form()
    n_items
    return n_items,


@app.cell
def __(mo):
    mo.md(
        """
        Now write the info of the tickets.
        """
    )
    return


@app.cell
def __():
    import json
    from pathlib import Path

    JSONS_FOLDER = Path("/Users/davidflorezmazuera/Library/CloudStorage/OneDrive-UNIVERSIDADDEMURCIA/UNIVERSIDAD/Universidad/Computacion/tfg/manualTicketParse/GT")

    def save_ticket(to_save, id):
        with open(JSONS_FOLDER.joinpath(f"{id}-ticket.json"), "w") as f:
            json.dump(to_save, f)
        print("saved")
    return JSONS_FOLDER, Path, json, save_ticket


@app.cell
def __(mo, n_items, save_ticket, ticket_id):
    item = mo.ui.dictionary({
        "nm":mo.ui.text(),
        "cnt":mo.ui.text(),
        "price":mo.ui.text()}, label="item")
    subtotal = mo.ui.dictionary({
        "subtotal_price" : mo.ui.text(placeholder="subtotal price"),
        "service_price" : mo.ui.text(placeholder="service price"),
        "tax_price" : mo.ui.text(placeholder="tax price"),
        "etc" : mo.ui.text(placeholder="etc"),
    })
    total = mo.ui.dictionary({"total_price":mo.ui.text(placeholder="total")})
    n = int(n_items.value)
    ticket = mo.ui.dictionary({
        "menu": mo.ui.array([ item for _ in range(n)]),
        "sub_total": subtotal,
        "total": total
    },label="ground_truth").form(
        on_change=lambda x : save_ticket(x, ticket_id.value)
    )
    return item, n, subtotal, ticket, total


@app.cell
def __(ticket_image):
    ticket_image
    return


@app.cell
def __(ticket):
    #test = mo.Html(
    #    f"""
    #        <div style="width:100%">
    #        {ticket}
    #        </div>
    #        <div style="width:100%; display:flex; align-items:center; ">
    #        {ticket_image}
    #        </div>
    #    """
    #)
    #test.style({"width":"90vw", "display":"flex","gap":"10px"})

    ticket

    return


if __name__ == "__main__":
    app.run()
