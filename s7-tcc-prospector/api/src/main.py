#!/usr/bin/env python3

if __name__ == "__main__":
    # ### Built-in deps
    # ### Third-party deps
    import uvicorn

    # ### Local deps
    from app.config import get_app_config


    settings = get_app_config()

    uvicorn.run(
        "app.setup:app", 
        host=settings.HOST, 
        port=settings.PORT, 
        reload=settings.RELOAD, 
        workers=settings.N_WORKERS,
        log_level=settings.LOG_LEVEL.lower(),
        forwarded_allow_ips='*'
    )
