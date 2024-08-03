from asyncio import run
from teo import App, Response, RequestCtx
from entities import EchoPathArguments


async def main():
  app = App()

  def hello_handler(_ctx):
    return Response.html("""
            <html>
                <head>
                    <title>Hello, Teo handlers</title>
                </head>
                <body>
                    <h1>Hello, Teo handlers!</h1>
                </body>
            </html>
        """)

  app.main_namespace().define_handler('hello', hello_handler)

  def empty_handler(_ctx):
    return Response.empty()

  app.main_namespace().define_handler('empty', empty_handler)

  def echo_handler(ctx: RequestCtx):
    path_arguments: EchoPathArguments = ctx.path_arguments()
    return Response.string(path_arguments['data'], 'text/plain')

  app.main_namespace().define_handler('echo', echo_handler)
  await app.run()


run(main())
