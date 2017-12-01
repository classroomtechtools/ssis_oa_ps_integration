import click


class Object(object):
    def __init__(self):
        # chance to get setings
        pass

    # define common methods here


@click.group()
@click.pass_context
def main(ctx):
    # Doesn't do much now, but leave it as boilerplate for when there are global flags n such
    ctx.obj = Object()


@main.command('go')
@click.pass_obj
def go(obj):
    """
    DOOO IT
    """ 
    from app.interface import OADownloader
    oa = OADownloader()
    oa.download()




