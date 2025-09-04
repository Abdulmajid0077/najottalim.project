from sqlalchemy import String, Text, Integer, ForeignKey, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .config import *
import enum


class FreeConsultation(Base):
    __tablename__="free_consultations"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(100))
    phone_number: Mapped[str] = mapped_column(String(13))

    def __repr__(self):
        return self.full_name
    
class CaruselAd(Base):
    __tablename__="carusel_ad"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)

    def __repr__(self):
        return self.title

    
class Category(Base):
    __tablename__="category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    courses: Mapped[list["Course"]] = relationship(back_populates="category")

    blog: Mapped[list["Course"]] = relationship(back_populates="category")

    def __repr__(self):
        return self.name
    
class CourseTypeChoise(str, enum.Enum):
    STANDARD = "Standart"
    BOOTCAMP = "Bootcamp"
    OTHER = "Other"
    
class Course(Base):
    __tablename__="courses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    duration: Mapped[int] = mapped_column(Integer())
    description: Mapped[str] = mapped_column(String(100))
    logo_path: Mapped[str] = mapped_column(String(200))
    technologies: Mapped[str] = mapped_column(Text())
    price: Mapped[int] = mapped_column(Integer())
    category_id: Mapped[int] = mapped_column(Integer(), ForeignKey("category.id"))
    course_type: Mapped[str] = mapped_column(Enum(CourseTypeChoise), default=CourseTypeChoise.STANDARD)

    category: Mapped["Category"] = relationship(back_populates="courses")

    def __repr__(self):
        return self.name
    
class Blog(Base):
    __tablename__="blog"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(Text())
    content: Mapped[str] = mapped_column(Text())
    blog_path: Mapped[str] = mapped_column(String(200))
    created_at: Mapped[DateTime] = mapped_column(DateTime)
    wievs: Mapped[int] = mapped_column(Integer, default=0)

    category: Mapped["Category"] = relationship(back_populates="blog")

class Comment(Base):
    __tablename__="comment"

    id: Mapped[int] = mapped_column(primary_key=True)
    comment_text: Mapped[str] = mapped_column(Text())
    user_id: Mapped[int] = mapped_column(Integer(), ForeignKey("user.id"))

class User(Base):
    __tablename__="user"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(String(50))
    job: Mapped[str] = mapped_column(String(100))
