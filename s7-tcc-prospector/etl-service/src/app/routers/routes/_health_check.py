# ### Built-in deps
# ### Third-party deps
from fastapi import APIRouter

# ### Local deps


router = APIRouter(tags=["Health Check"], prefix="")


@router.get("/", response_model=str)
def health_check():
    return "Server is running"
