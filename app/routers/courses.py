from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from .. import db
from ..models import Course, CourseCreate, CourseUpdate
from ..utils import paginate

router = APIRouter(prefix="/courses", tags=["Courses"])

@router.get("/", response_model=dict)
def list_courses_endpoint(
    page: Optional[int] = Query(None, description="Page number (1-based)"),
    limit: Optional[int] = Query(None, description="Items per page (max 100)")
):
    items, total = paginate(db.list_courses(), page, limit)
    return {"total": total, "page": page or 1, "limit": limit or 10, "items": items}

@router.get("/{course_id}", response_model=Course)
def get_course_endpoint(course_id: int):
    course = db.get_course(course_id)
    if not course:
        raise HTTPException(404, "Course not found")
    return course

@router.post("/", response_model=Course, status_code=201)
def create_course_endpoint(payload: CourseCreate):
    return db.create_course(payload)

@router.put("/{course_id}", response_model=Course)
def update_course_endpoint(course_id: int, payload: CourseUpdate):
    course = db.update_course(course_id, payload)
    if not course:
        raise HTTPException(404, "Course not found")
    return course

@router.delete("/{course_id}", status_code=204)
def delete_course_endpoint(course_id: int):
    ok = db.delete_course(course_id)
    if not ok:
        raise HTTPException(404, "Course not found")
    return
