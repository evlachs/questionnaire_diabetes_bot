import aiohttp_jinja2
from web_server import templates


@aiohttp_jinja2.template('templates/index.html')
async def index(request):
    return {'title': 'Пишем первое приложение на aiohttp'}
