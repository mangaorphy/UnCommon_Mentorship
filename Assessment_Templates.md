# Assessment Templates and Project Ideas 📝

## 🎯 **Assessment Framework Overview**

This document provides ready-to-use assessment templates for each phase of the Python to Django REST Framework course. Each assessment is designed to test specific learning objectives and can be adapted based on class pace and student needs.

---

## 📅 **Phase 1: Python Fundamentals (Weeks 1-4)**

### **Week 1 Assessment: Variables and Data Types**

#### **Quiz Questions (15 minutes)**

1. **Multiple Choice**: What is the correct way to create a variable in Python?
   - a) `var name = "John"`
   - b) `name = "John"`
   - c) `string name = "John"`
   - d) `name := "John"`

2. **Code Completion**: Fill in the blanks:
   ```python
   age = ____  # An integer
   height = ____  # A float
   is_student = ____  # A boolean
   name = ____  # A string
   ```

3. **Error Detection**: What's wrong with this code?
   ```python
   1student_name = "Alice"
   age = "twenty"
   total = age + 5
   ```

#### **Practical Exercise (30 minutes)**

**Project: Personal Information System**

Create a Python program that:
1. Stores information about a person (name, age, city, favorite color)
2. Calculates their birth year
3. Creates a formatted introduction message
4. Displays all information in a user-friendly format

**Expected Output:**
```
=== Personal Information ===
Name: Alice Johnson
Age: 22 years old
Birth Year: 2003
City: New York
Favorite Color: Blue

Introduction: "Hi! I'm Alice Johnson from New York. I'm 22 years old and my favorite color is blue."
```

**Grading Rubric:**
- Variables correctly defined (25%)
- Proper data types used (25%)
- Calculations correct (25%)
- Output formatting (25%)

---

### **Week 2 Assessment: Control Flow and Functions**

#### **Coding Challenges (45 minutes)**

**Challenge 1: Grade Calculator (15 minutes)**
```python
def calculate_grade(score):
    """
    Calculate letter grade from numeric score
    A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
    """
    # Student implements this function
    pass

# Test cases
print(calculate_grade(95))  # Should print "A"
print(calculate_grade(73))  # Should print "C"
print(calculate_grade(45))  # Should print "F"
```

**Challenge 2: Number Guessing Game (30 minutes)**

Create a number guessing game with:
- Random number between 1-100
- Maximum 7 attempts
- Hints (too high/too low)
- Win/lose messages
- Option to play again

**Assessment Criteria:**
- Correct use of loops (30%)
- Proper conditionals (30%)
- Function organization (20%)
- User experience (20%)

---

### **Week 3 Assessment: Data Structures**

#### **Project: Student Management System (60 minutes)**

Create a student management system using Python data structures:

```python
# Sample data structure
students = [
    {
        "id": 1,
        "name": "Alice Johnson",
        "grades": [85, 92, 78, 96],
        "subjects": ["Math", "Science", "English", "History"]
    },
    # More students...
]

# Required functions to implement:
def add_student(students, name, subjects):
    """Add a new student to the system"""
    pass

def add_grade(students, student_id, grade):
    """Add a grade to a student"""
    pass

def calculate_average(students, student_id):
    """Calculate student's average grade"""
    pass

def get_top_students(students, n=3):
    """Get top N students by average"""
    pass

def search_student(students, name):
    """Find student by name"""
    pass
```

**Bonus Features:**
- Remove student functionality
- Grade statistics (highest, lowest, class average)
- Export data to text file

---

### **Week 4 Assessment: Files and Modules**

#### **Project: Personal Finance Tracker (90 minutes)**

Create a personal finance application that:

**Core Requirements:**
1. **Transaction Management**
   - Add income/expense transactions
   - Categories (Food, Transport, Entertainment, etc.)
   - Date tracking

2. **Data Persistence**
   - Save/load data from CSV file
   - Backup functionality

3. **Reporting**
   - Monthly spending by category
   - Income vs expenses
   - Savings calculation

4. **Modular Design**
   - Separate modules for different functionalities
   - Clean code organization

**File Structure:**
```
finance_tracker/
├── main.py              # Main application
├── transaction.py       # Transaction class
├── file_manager.py      # File operations
├── reports.py           # Reporting functions
├── data/
│   ├── transactions.csv
│   └── backup.csv
└── requirements.txt
```

**Sample Usage:**
```python
# main.py
from transaction import Transaction
from file_manager import save_data, load_data
from reports import monthly_report, category_breakdown

def main():
    transactions = load_data("data/transactions.csv")
    
    while True:
        print("\n1. Add Transaction")
        print("2. View Report")
        print("3. Save & Exit")
        
        choice = input("Choose option: ")
        # Handle user input...

if __name__ == "__main__":
    main()
```

---

## 📅 **Phase 2: Object-Oriented Programming (Weeks 5-6)**

### **Week 5-6 Assessment: OOP Library System**

#### **Project: Library Management System (120 minutes)**

Create a comprehensive library system using OOP principles:

**Class Hierarchy:**
```python
class Person:
    """Base class for library users"""
    def __init__(self, name, email, phone):
        # Implementation required
        pass

class Member(Person):
    """Library member who can borrow books"""
    def __init__(self, name, email, phone, member_id):
        # Implementation required
        pass
    
    def borrow_book(self, book):
        # Implementation required
        pass
    
    def return_book(self, book):
        # Implementation required
        pass

class Librarian(Person):
    """Library staff member"""
    def __init__(self, name, email, phone, employee_id):
        # Implementation required
        pass
    
    def add_book(self, book):
        # Implementation required
        pass
    
    def remove_book(self, book_id):
        # Implementation required
        pass

class Book:
    """Represents a book in the library"""
    def __init__(self, title, author, isbn, copies=1):
        # Implementation required
        pass
    
    def is_available(self):
        # Implementation required
        pass

class Library:
    """Main library system"""
    def __init__(self, name):
        # Implementation required
        pass
    
    def register_member(self, member):
        # Implementation required
        pass
    
    def find_book(self, title=None, author=None, isbn=None):
        # Implementation required
        pass
    
    def generate_report(self):
        # Implementation required
        pass
```

**Required Features:**
1. **Book Management**
   - Add/remove books
   - Search by title, author, or ISBN
   - Track availability

2. **Member Management**
   - Register new members
   - Track borrowed books
   - Calculate late fees

3. **Transaction System**
   - Borrow/return operations
   - Due date tracking
   - History logging

4. **Reporting**
   - Most popular books
   - Member statistics
   - Overdue books

**Assessment Criteria:**
- Proper class design (25%)
- Inheritance implementation (20%)
- Encapsulation and data protection (20%)
- Method implementation (20%)
- Code organization and documentation (15%)

---

## 📅 **Phase 3: Django Fundamentals (Weeks 8-10)**

### **Week 8 Assessment: Django Basics**

#### **Project: Personal Portfolio Website (90 minutes)**

Create a personal portfolio website with:

**Required Pages:**
1. **Home Page**
   - Welcome message
   - Brief introduction
   - Navigation menu

2. **About Page**
   - Personal information
   - Skills and experience
   - Education background

3. **Projects Page**
   - List of projects
   - Project descriptions
   - Links to code/demos

4. **Contact Page**
   - Contact information
   - Contact form (basic)

**Technical Requirements:**
- Proper URL routing
- Template inheritance
- Static file handling
- Responsive design
- Clean HTML/CSS

**Assessment Criteria:**
- URL configuration (20%)
- View implementation (25%)
- Template design (25%)
- Static files integration (15%)
- Overall presentation (15%)

---

### **Week 9 Assessment: Models and Database**

#### **Project: Blog Application (120 minutes)**

Create a blog application with database integration:

**Models to Implement:**
```python
# models.py
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

**Required Features:**
1. **Admin Interface**
   - Custom admin panels for all models
   - Proper list displays and filters
   - Search functionality

2. **Views and Templates**
   - Blog post list (with pagination)
   - Post detail view
   - Category-wise filtering
   - Tag-based filtering

3. **Database Operations**
   - Complex queries using Django ORM
   - Proper relationship handling
   - Data validation

**Advanced Features (Bonus):**
- Search functionality
- Popular posts (by comment count)
- Archive by date
- RSS feed

---

### **Week 10 Assessment: Forms and Authentication**

#### **Project: Task Management System (150 minutes)**

Create a task management system with user authentication:

**Core Features:**
1. **User Authentication**
   - User registration
   - Login/logout
   - Password reset
   - User profiles

2. **Task Management**
   - Create, edit, delete tasks
   - Task categories and priorities
   - Due dates and reminders
   - Task completion tracking

3. **Collaboration**
   - Share tasks with other users
   - Task comments
   - Assignment notifications

**Models:**
```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, related_name='assigned_tasks')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    due_date = models.DateTimeField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
```

**Assessment Criteria:**
- Authentication implementation (25%)
- Form handling and validation (25%)
- Model design and relationships (20%)
- User experience and interface (20%)
- Security considerations (10%)

---

## 📅 **Phase 4: Django REST Framework (Weeks 11-14)**

### **Week 11-12 Assessment: API Development**

#### **Project: Recipe Sharing API (180 minutes)**

Create a comprehensive recipe sharing API:

**API Endpoints:**
```
GET    /api/recipes/              # List all recipes
POST   /api/recipes/              # Create new recipe
GET    /api/recipes/{id}/         # Get recipe details
PUT    /api/recipes/{id}/         # Update recipe
DELETE /api/recipes/{id}/         # Delete recipe

GET    /api/categories/           # List categories
GET    /api/ingredients/          # List ingredients
GET    /api/users/{id}/recipes/   # User's recipes

# Search and filtering
GET    /api/recipes/?search=pasta
GET    /api/recipes/?category=dessert
GET    /api/recipes/?difficulty=easy
```

**Models:**
```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    
class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField()  # in minutes
    cook_time = models.IntegerField()  # in minutes
    servings = models.IntegerField()
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='recipes/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.CharField(max_length=50)
```

**Required Features:**
1. **CRUD Operations** for all models
2. **Authentication** with tokens
3. **Permissions** (users can only edit their recipes)
4. **Filtering and Search**
5. **Pagination**
6. **API Documentation**

**Assessment Criteria:**
- API design and RESTful principles (25%)
- Serializer implementation (20%)
- Authentication and permissions (20%)
- Code quality and organization (20%)
- Documentation and testing (15%)

---

### **Week 13-14 Assessment: Advanced API Features**

#### **Project: Social Media API (240 minutes)**

Create a social media platform API with advanced features:

**Core Features:**
1. **User Management**
   - User profiles with avatars
   - Follow/unfollow system
   - User verification

2. **Post System**
   - Text posts with images
   - Like and comment system
   - Post sharing/reposting
   - Hashtag support

3. **Real-time Features**
   - Activity feeds
   - Notifications
   - Direct messaging (basic)

4. **Advanced API Features**
   - JWT authentication
   - Rate limiting
   - API versioning
   - Comprehensive permissions

**Sample API Structure:**
```
# Authentication
POST   /api/v1/auth/register/
POST   /api/v1/auth/login/
POST   /api/v1/auth/refresh/
POST   /api/v1/auth/logout/

# Users
GET    /api/v1/users/profile/
PUT    /api/v1/users/profile/
POST   /api/v1/users/{id}/follow/
POST   /api/v1/users/{id}/unfollow/
GET    /api/v1/users/{id}/followers/
GET    /api/v1/users/{id}/following/

# Posts
GET    /api/v1/posts/              # Feed
POST   /api/v1/posts/              # Create post
GET    /api/v1/posts/{id}/         # Post detail
PUT    /api/v1/posts/{id}/         # Update post
DELETE /api/v1/posts/{id}/         # Delete post
POST   /api/v1/posts/{id}/like/    # Like post
POST   /api/v1/posts/{id}/comment/ # Comment on post

# Search and Discovery
GET    /api/v1/search/?q=term
GET    /api/v1/trending/hashtags/
GET    /api/v1/posts/?hashtag=tech
```

**Assessment Criteria:**
- API complexity and completeness (30%)
- Security implementation (25%)
- Performance and optimization (20%)
- Code architecture (15%)
- Testing coverage (10%)

---

## 📅 **Final Capstone Project (Weeks 15-16)**

### **Choose Your Adventure: Capstone Projects**

Students select one of these comprehensive projects:

#### **Option 1: E-Learning Platform**
- Course management system
- Video streaming capability
- Progress tracking
- Certificates generation
- Payment integration

#### **Option 2: E-commerce Platform**
- Product catalog with images
- Shopping cart and checkout
- Order management
- Payment processing
- Inventory tracking

#### **Option 3: Project Management Tool**
- Team collaboration features
- Task assignment and tracking
- Time logging
- Reporting and analytics
- File sharing

#### **Option 4: Healthcare Management System**
- Patient records management
- Appointment scheduling
- Medical history tracking
- Prescription management
- Report generation

### **Capstone Assessment Rubric**

| Criteria | Excellent (A) | Good (B) | Satisfactory (C) | Needs Improvement (D/F) |
|----------|---------------|----------|------------------|-------------------------|
| **Code Quality** | Clean, well-documented, follows best practices | Good structure, minimal issues | Functional but needs improvement | Poor structure, hard to understand |
| **Functionality** | All features work perfectly | Most features work well | Basic features work | Many features broken |
| **API Design** | RESTful, well-designed endpoints | Good API structure | Basic API functionality | Poor API design |
| **Security** | Comprehensive security measures | Good security practices | Basic security implemented | Security vulnerabilities |
| **Testing** | Comprehensive test coverage | Good test coverage | Basic tests | Minimal or no tests |
| **Documentation** | Excellent documentation | Good documentation | Basic documentation | Poor or missing documentation |
| **Deployment** | Successfully deployed and accessible | Deployed with minor issues | Deployment attempted | Not deployed |
| **Presentation** | Clear, professional presentation | Good presentation skills | Adequate presentation | Poor presentation |

### **Final Project Timeline**

**Week 15:**
- Day 1-2: Project planning and setup
- Day 3-4: Core model and API development
- Day 5: Mid-week progress check

**Week 16:**
- Day 1-2: Advanced features and testing
- Day 3: Deployment and documentation
- Day 4: Final testing and bug fixes
- Day 5: Project presentations

---

## 📊 **Overall Course Assessment**

### **Grade Distribution:**
- Weekly Assessments: 40%
- Milestone Projects: 35%
- Final Capstone: 20%
- Participation and Improvement: 5%

### **Final Grade Scale:**
- A: 90-100% (Exceptional understanding and application)
- B: 80-89% (Good understanding with minor gaps)
- C: 70-79% (Adequate understanding, needs practice)
- D: 60-69% (Below expectations, significant gaps)
- F: Below 60% (Does not meet course objectives)

---

## 🎯 **Success Metrics**

By course completion, students should demonstrate:
- [ ] Ability to write clean, maintainable Python code
- [ ] Understanding of OOP principles and design patterns
- [ ] Proficiency in Django web development
- [ ] Competency in building REST APIs with DRF
- [ ] Knowledge of testing and deployment practices
- [ ] Confidence to continue learning independently

---

**Remember**: These assessments are designed to be challenging but achievable. Adjust difficulty and time requirements based on your specific class needs and student progress. The goal is learning, not just testing! 🚀
