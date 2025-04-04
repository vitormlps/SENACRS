# ### Built-in deps
# ### Third-party deps
from starlette.responses import JSONResponse

# ### Local deps


async def http_exc_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )


async def generic_exc_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": str(exc)},
    )
