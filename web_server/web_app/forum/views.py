import aiohttp_jinja2
from web_server import templates


@aiohttp_jinja2.template('index.html')
async def index(request):
    return {'title': 'Пишем первое приложение на aiohttp'}
