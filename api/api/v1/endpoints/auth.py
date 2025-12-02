from fastapi import APIRouter, Depends, HTTPException
from supabase import Client
from ..schemas.auth import UserCreate, Token
from ....core.supabase_client import get_supabase_client

router = APIRouter()

@router.post("/register", response_model=Token)
def register_user(user_in: UserCreate, supabase: Client = Depends(get_supabase_client)):
    """
    Create a new user.
    """
    try:
        # Create user in auth.users
        res = supabase.auth.sign_up({
            "email": user_in.email,
            "password": user_in.password,
        })

        if res.user is None:
             raise HTTPException(status_code=400, detail="Could not create user")

        user_id = res.user.id
        
        # Insert public profile
        supabase.table("profiles").insert({
            "id": user_id,
            "name": user_in.name
        }).execute()

        # Return JWT token
        return {
            "access_token": res.session.access_token,
            "token_type": "bearer"
        }

    except Exception as e:
        # This is a generic catch. In a real app, you'd want to handle specific
        # Supabase exceptions, like for a user already existing.
        if "already registered" in str(e).lower():
             raise HTTPException(status_code=400, detail="Email already registered")
        raise HTTPException(status_code=500, detail=str(e))
