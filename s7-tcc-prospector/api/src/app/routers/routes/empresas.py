# ### Built-in deps
from typing import List

# ### Third-party deps
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse

# ### Local deps
from ...security.current_user_auth import validate_token
from ...entities.empresas.repository import empresas_repo, EmpresasView, EmpresasFilter, EmpresasMainView
from ...helpers.clean_folder import clean_exports_folder


router = APIRouter(tags=["Empresas"], prefix="/empresas")


@router.get("", response_model=List[EmpresasMainView])
def get_all_by(
    query: EmpresasFilter = Depends(EmpresasFilter),
    current_user_id: str = Depends(validate_token),
):
    result = empresas_repo().get_all_by(filters=query)

    if len(result) == 0:
        raise HTTPException(404, "Empresas not found")

    return result


@router.get("/count")
def get(current_user_id: str = Depends(validate_token)):
    result = empresas_repo().count()

    if result is None:
        raise HTTPException(404, "Empresas not found")

    return result


@router.get("/{id}", response_model=EmpresasView)
def get(
    id: str,
    current_user_id: str = Depends(validate_token)
):
    result = empresas_repo().get(id)

    if result is None:
        raise HTTPException(404, "Empresa not found")

    return result


@router.post("/export", response_class=FileResponse)
def generate_csv(
    payload: List[str],
    current_user_id: str = Depends(validate_token)
):
    clean_exports_folder()

    file_path, file_name = empresas_repo().generate_csv(payload)

    return FileResponse(
        path=file_path + file_name,
        filename=file_name,
        media_type="application/vnd.ms-excel",
    )
