from typing import List, Optional
from .models import Course, CourseCreate, CourseUpdate

# pretend DB
_courses: List[Course] = []
_next_id = 1

def seed():
    global _next_id
    demo = [
        {"title": "FastAPI Basics", "description": "Routing, params, docs"},
        {"title": "Python Crash", "description": "Syntax + types"},
        {"title": "Async IO Intro", "description": "await, tasks"},
        {"title": "Testing 101", "description": "pytest basics"},
    ]
    for c in demo:
        create_course(CourseCreate(**c))

def list_courses() -> List[Course]:
    return list(_courses)

def get_course(cid: int) -> Optional[Course]:
    return next((c for c in _courses if c.id == cid), None)

def create_course(payload: CourseCreate) -> Course:
    global _next_id
    course = Course(id=_next_id, **payload.model_dump())
    _courses.append(course)
    _next_id += 1
    return course

def update_course(cid: int, payload: CourseUpdate) -> Optional[Course]:
    c = get_course(cid)
    if not c:
        return None
    data = c.model_dump()
    for k, v in payload.model_dump(exclude_unset=True).items():
        data[k] = v
    idx = _courses.index(c)
    _courses[idx] = Course(**data)
    return _courses[idx]

def delete_course(cid: int) -> bool:
    c = get_course(cid)
    if not c:
        return False
    _courses.remove(c)
    return True
