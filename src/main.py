
"""
Student Manager — DevOps Lab 5
Module: Search Student
"""

from student import Student


def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo mã hoặc tên."""

    keyword = keyword.strip().lower()

    if not keyword:
        print("Vui long nhap tu khoa tim kiem!")
        return []

    results = []

    for student in students:
        if (keyword in student.student_id.lower()
                or keyword in student.name.lower()):
            results.append(student)

    return results


def main():
    print("=" * 50)
    print("STUDENT MANAGER — SEARCH STUDENT")
    print("=" * 50)

    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
        Student("SV004", "Pham Thi D", 22, "K19"),
    ]

    # Tìm kiếm sinh viên
    keyword = "Tran"
    results = search_student(students, keyword)

    print(f"\nKet qua tim kiem: {keyword}")

    if results:
        for student in results:
            print(student)
        print(f"Tim thay {len(results)} sinh vien.")
    else:
        print("Khong tim thay sinh vien.")


if __name__ == "__main__":
    main()

"""
Student Manager — DevOps Lab 5
Module: Main Application
"""

from student import Student


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)

    # Tạo danh sách sinh viên mẫu
    students = [
        Student("SV001", "Nguyen Van A", 20, "K20"),
        Student("SV002", "Tran Thi B", 21, "K20"),
        Student("SV003", "Le Van C", 19, "K21"),
    ]

    # Hiển thị danh sách sinh viên
    for student in students:
        print(f"  {student}")

    print(f"\nTotal: {len(students)} students")


if __name__ == "__main__":
    main()
