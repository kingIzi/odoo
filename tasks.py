from invoke import task


@task
def start(
    c,
    database="rd-demo",
    modules="",
    addons_path="addons/,~/projects/odoo/odoo-tutorials/odoo-tutorials",
):
    """
    Start Odoo with configurable parameters.

    Parameters:
        database:     The database name (-d)
        modules:      Comma-separated list of modules to update (-u)
        addons_path:  Comma-separated list of addon paths (--addons-path)
    """
    cmd = f'./odoo-bin --addons-path="{addons_path}" -d {database}'

    if modules:
        cmd += f" -u {modules}"

    c.run(cmd)
