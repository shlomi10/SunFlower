# 🧪 QA Automation Test Suite

[![Python](https://img.shields.io/badge/Python-3.13.5+-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-2D8CFF?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-FF6C37?style=for-the-badge&logo=qameta&logoColor=white)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

> 🚀 **Comprehensive E-commerce Automation Testing Suite with Page Object Model Pattern**

A modern, robust automation testing framework built with **Playwright** and **Python** for testing e-commerce functionalities. Features comprehensive test reporting with **Allure**, containerized execution with **Docker**, and follows industry best practices.

## ✨ Test Scenario Coverage

### 🎯 **End-to-End User Journey Testing**
- **User Registration**: Complete registration flow with validation
- **Authentication Verification**: Email presence validation in header
- **Product Discovery**: Digital downloads catalog navigation  
- **Shopping Cart Functionality**: Random product selection and cart verification
- **Data Integrity**: Product name consistency across pages

### 📋 **Test Standard Documentation**

#### **Test Purpose**
Validate the complete user registration and shopping cart workflow on the demo webshop, ensuring data consistency and proper navigation flow.

#### **Preconditions**
- Demo webshop (https://demowebshop.tricentis.com) must be accessible
- Browser environment with internet connectivity
- Valid test data generation capabilities

#### **Test Steps & Expected Results**
1. **Navigate to Application** → Homepage loads successfully
2. **User Registration** → Registration form accepts valid data
3. **Email Validation** → User email appears in header after registration
4. **Product Selection** → Random digital download can be selected
5. **Cart Operations** → Product successfully added to shopping cart
6. **Data Verification** → Product name matches across product page and cart

#### **Post-Conditions**
- Test user account created in system
- Shopping cart contains selected product
- Browser session terminated cleanly

#### **Validation Criteria**
- ✅ Registration completes without errors
- ✅ User email displays correctly in header
- ✅ Product name consistency between selection and cart
- ✅ All navigation flows execute successfully

## 🏗️ Architecture & Design Patterns

### **Page Object Model (POM)**
```
📁 pages/
├── 🏠 basePage.py          # Common page interactions
├── 🏡 homePage.py          # Homepage specific actions
├── 📝 registerPage.py      # Registration form handling
├── 💿 digitalDownloadsPage.py # Product catalog interactions
└── 🛒 shoppingCartPage.py  # Shopping cart operations
```

### **Test Structure**
```
📁 tests/
├── 🧪 test_overall.py      # Main test scenarios
├── 🔧 base_class.py        # Test base class with common setup
└── ⚙️ conftest.py          # Pytest configuration & fixtures
```

### **Design Principles**
- **Single Responsibility**: Each page class handles specific UI interactions
- **DRY (Don't Repeat Yourself)**: Common actions abstracted in BasePage
- **Maintainability**: Clear separation of concerns between test logic and page interactions
- **Scalability**: Easy to extend with additional page objects and test scenarios

## 🚀 Quick Start

### Prerequisites
- **Python 3.13.5+**
- **Docker & Docker Compose**
- **Git**

### 1. Clone Repository
```bash
git clone https://github.com/shlomi10/sunFlower.git
cd sunflower
```

### 2. Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install

# Run tests locally
pytest --alluredir=allure-results
```

### 3. Docker Execution (Recommended)
```bash
# Run complete test suite with reporting
docker-compose up

# View Allure reports
open http://localhost:5050
```

## 🛠️ Tech Stack

### **Core Framework**
- **[Playwright](https://playwright.dev/)** - Modern browser automation with fast, reliable cross-browser testing
- **[Python 3.13.5+](https://www.python.org/)** - Latest Python features for robust test development
- **[Pytest](https://pytest.org/)** - Advanced testing framework with powerful fixtures and plugins

### **Test Enhancement**
- **[Faker](https://faker.readthedocs.io/)** - Dynamic test data generation for realistic scenarios
- **[Allure](https://docs.qameta.io/allure/)** - Comprehensive test reporting with rich visualizations
- **[pytest-playwright](https://playwright.dev/python/docs/test-runners)** - Seamless Playwright-Pytest integration

### **DevOps & Infrastructure**
- **[Docker](https://www.docker.com/)** - Containerized test execution for consistency
- **[Docker Compose](https://docs.docker.com/compose/)** - Multi-service orchestration for tests and reporting
- **[Xvfb](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml)** - Virtual display for headless browser execution

## 🧪 Test Execution Options

### **Local Development**
```bash
# Run specific test
pytest tests/test_overall.py::TestOverall::test_register_and_add_item_to_shopping_cart -v

# Run with detailed output
pytest --tb=short --alluredir=allure-results

# Generate and serve Allure report
allure serve allure-results
```

### **Headless Execution**
```bash
# Run in headless mode
pytest --headed=false

# Run with custom browser
pytest --browser=firefox
```

### **Docker with Custom Options**
```bash
# Run with custom environment
docker-compose run tests pytest tests/ -v --tb=short

# Debug mode with display
docker-compose run tests pytest tests/ --headed
```

## 📊 Test Reporting

### **Allure Features**
- 📈 **Test Execution Dashboard** - Overview of test results and trends
- 📋 **Detailed Test Steps** - Step-by-step execution with screenshots
- 📸 **Visual Evidence** - Automatic screenshots on failures
- 🎯 **Test Categories** - Organized by Epic, Feature, and Story
- ⏱️ **Performance Metrics** - Execution time analysis

### **Report Access**
- **Local**: Run `allure serve allure-results`
- **Docker**: Navigate to `http://localhost:5050`
- **CI/CD**: Reports automatically generated and archived

## 🔧 Configuration

### **Environment Variables** (`.env`)
```env
BASE_URL=https://demowebshop.tricentis.com/
```

### **Pytest Configuration**
- **Automatic fixtures** for browser setup/teardown
- **Screenshot capture** on test failures  
- **Trace collection** for debugging
- **Flaky test handling** with automatic reruns

### **Browser Settings**
- **Maximized window** for consistent element visibility
- **No viewport restrictions** for responsive testing
- **Tracing enabled** for detailed debugging
- **Screenshot support** for visual validation

## 🧩 Key Components

### **BasePage Class**
```python
# Common page interactions
- navigate(url)
- click(element)  
- click_on_random_element(elements)
- type(element, text)
- get_text(element)
- is_visible(element)
- take_screenshot()
```

### **Test Utilities**
```python
# Dynamic test data
faker.first_name()
faker.last_name() 
faker.email()
faker.password()
```

### **Allure Integration**
```python
@allure.epic("Functionality")
@allure.feature("E-commerce Testing")
@allure.story("User Registration & Shopping")
@allure.step("Validate registration flow")
```

## 🏃‍♂️ CI/CD Integration

### **GitHub Actions Example**
```yaml
name: E2E Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Tests
        run: docker-compose up --abort-on-container-exit
      - name: Publish Results
        uses: simple-elf/allure-report-action@master
```

### **Test Artifacts**
- **Allure Reports** - Comprehensive test execution reports
- **Screenshots** - Visual evidence of failures
- **Traces** - Detailed execution traces for debugging
- **Logs** - Structured logging for troubleshooting

## 🐛 Debugging & Troubleshooting

### **Common Issues**

**Browser Launch Failures:**
```bash
# Install browser dependencies
python -m playwright install-deps
```

**Element Not Found:**
```bash
# Run with slower execution
pytest --slowmo=1000
```

**Docker Permission Issues:**
```bash
# Fix volume permissions
sudo chown -R $USER:$USER ./allure-results ./screenshots ./trace
```

### **Debug Mode**
```bash
# Enable debug logging
pytest --log-cli-level=DEBUG

# Run with browser dev tools
pytest --headed --slowmo=1000
```

## 📈 Performance & Reliability

### **Execution Speed**
- **Parallel execution** support with pytest-xdist
- **Browser reuse** for faster test execution
- **Smart waiting** with Playwright's auto-wait functionality

### **Stability Features**
- **Flaky test handling** with automatic reruns
- **Robust element selection** with multiple locator strategies
- **Timeout management** with configurable wait times
- **Error recovery** with detailed failure reporting

## 🤝 Contributing

### **Development Workflow**
1. **Fork** the repository
2. **Create** feature branch (`git checkout -b feature/amazing-test`)
3. **Follow** coding standards and add appropriate Allure decorators
4. **Add tests** for new functionality
5. **Ensure** all tests pass locally
6. **Submit** pull request with detailed description

### **Coding Standards**
- Follow **PEP 8** Python style guide
- Use **meaningful** variable and method names
- Add **Allure** step decorations for better reporting
- Include **docstrings** for complex methods
- **Maintain** page object separation

## 📚 Documentation

### **API References**
- [Playwright Python API](https://playwright.dev/python/docs/api/class-playwright)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)

### **Learning Resources**
- [Page Object Model Best Practices](https://playwright.dev/docs/pom)
- [Playwright Testing Patterns](https://playwright.dev/docs/best-practices)
- [Python Testing with Pytest](https://pythontest.com/pytest-book/)

## 📄 License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2025 Shlomi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

- **Playwright Team** for the excellent browser automation framework
- **Pytest Community** for the robust testing ecosystem
- **Allure Framework** for comprehensive test reporting
- **Tricentis** for providing the demo webshop application

## 📞 Contact

**Shlomi** - [@shlomi10](https://github.com/shlomi10)

**Project Link**: [https://github.com/shlomi10/qa-automation-suite](https://github.com/shlomi10/qa-automation-suite)

---

⭐ **Star this repository if you found it helpful for your QA automation journey!**

![Footer](https://img.shields.io/badge/Made%20with-🧪%20&%20❤️-red?style=for-the-badge)



http://localhost:5051/allure-docker-service/projects/default/reports/latest/index.html