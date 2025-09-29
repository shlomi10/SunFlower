# 🧪 QA Automation Test Suite

[![Python](https://img.shields.io/badge/Python-3.13.5+-FFD43B?style=for-the-badge&logo=python&logoColor=3776AB)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-45BA4B?style=for-the-badge&logo=playwright&logoColor=white)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-009FE3?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-FF5C00?style=for-the-badge&logo=qameta&logoColor=white)](https://docs.qameta.io/allure/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Docker Hub](https://img.shields.io/badge/Docker_Hub-1D63ED?style=for-the-badge&logo=docker&logoColor=white)](https://hub.docker.com/r/shlomi10/sunflower)
[![Faker](https://img.shields.io/badge/Faker-9B59B6?style=for-the-badge&logo=python&logoColor=white)](https://faker.readthedocs.io/)
[![Live Report](https://img.shields.io/badge/📊_Live_Report-E74C3C?style=for-the-badge&logoColor=white)](http://localhost:5051/allure-docker-service/projects/default/reports/latest/index.html)
[![Status](https://img.shields.io/badge/Status-Active-2ECC71?style=for-the-badge)](https://github.com/shlomi10/sunFlower)

> 🚀 **Production-Ready E2E Automation Framework with Page Object Model & Advanced Reporting**

A modern, scalable automation testing framework built with **Playwright** and **Python** for comprehensive e-commerce testing. Features real-time test reporting with **Allure**, containerized execution with **Docker**, and follows SOLID principles and industry best practices.

---

## 📋 Table of Contents

- [Test Coverage](#-test-scenario-coverage)
- [Architecture](#️-architecture--design-patterns)
- [Quick Start](#-quick-start)
- [Tech Stack](#️-tech-stack)
- [Test Execution](#-test-execution-options)
- [Live Reporting](#-test-reporting--live-dashboard)
- [Configuration](#-configuration)
- [Docker Hub](#-docker-hub-image)
- [CI/CD Integration](#️-cicd-integration)
- [Contributing](#-contributing)

---

## ✨ Test Scenario Coverage

### 🎯 **End-to-End User Journey Testing**
This suite validates complete user workflows across the e-commerce platform:

- **User Registration Flow** 
  - Dynamic test data generation using Faker
  - Form validation and submission
  - Success confirmation handling

- **Authentication & Session Management**
  - Email presence validation in header post-registration
  - Session persistence verification
  - User context maintenance across pages

- **Product Discovery & Catalog Navigation**
  - Digital downloads section browsing
  - Random product selection for comprehensive coverage
  - Product page rendering validation

- **Shopping Cart Operations**
  - Add-to-cart functionality
  - Cart state management
  - Product quantity and details verification

- **Data Integrity & Consistency**
  - Product name consistency across product page and shopping cart
  - Cross-page data validation
  - UI synchronization checks

### 📋 **Test Standard Documentation**

#### **Test Purpose**
Validate the complete user registration and shopping cart workflow on the demo webshop (https://demowebshop.tricentis.com), ensuring data consistency, proper navigation flow, and system reliability across the entire user journey.

#### **Preconditions**
- ✅ Demo webshop must be accessible via HTTPS
- ✅ Browser environment with internet connectivity
- ✅ Valid test data generation capabilities (Faker library)
- ✅ Playwright browsers installed

#### **Test Steps & Expected Results**

| Step | Action | Expected Result | Validation |
|------|--------|-----------------|------------|
| 1 | Navigate to application | Homepage loads successfully | Page title and elements visible |
| 2 | Initiate registration | Registration form displays | All form fields accessible |
| 3 | Fill registration form | Form accepts valid input | No validation errors |
| 4 | Submit registration | Account created successfully | Success message displayed |
| 5 | Verify authentication | User email visible in header | Email matches registered data |
| 6 | Navigate to digital downloads | Category page loads | Products displayed correctly |
| 7 | Select random product | Product details page opens | Product information visible |
| 8 | Add product to cart | Item added confirmation | Success notification appears |
| 9 | Navigate to shopping cart | Cart page displays | Selected product visible |
| 10 | Verify cart data | Product details match | Name, price consistency validated |

#### **Post-Conditions**
- Test user account created in system database
- Shopping cart contains selected product with correct details
- Browser session terminated cleanly with no memory leaks
- Test artifacts (screenshots, traces) saved for analysis

#### **Validation Criteria**
- ✅ Registration completes without errors (HTTP 200/201)
- ✅ User email displays correctly in header element
- ✅ Product name consistency: `product_page_title === cart_item_title`
- ✅ All navigation flows execute within acceptable timeout limits (< 5s per step)
- ✅ No JavaScript console errors during execution
- ✅ All assertions pass with 100% success rate

---

## 🗺️ Architecture & Design Patterns

### **Page Object Model (POM)**
Implements a clean separation between test logic and UI interactions:

```
📁 pages/
├── 🏠 basePage.py              # Base class with common page interactions
│   ├── navigate(url)           # Navigate to specific URL
│   ├── click(element)          # Click on element
│   ├── click_on_random_element()  # Random element selection
│   ├── type(element, text)     # Type text into input fields
│   ├── get_text(element)       # Extract text content
│   ├── is_visible(element)     # Check element visibility
│   ├── wait_for_loader()       # Wait for loading spinners
│   └── take_screenshot()       # Capture page screenshots
│
├── 🏡 homePage.py               # Homepage specific actions
│   ├── select_register()       # Navigate to registration
│   ├── get_registered_email()  # Verify logged-in user
│   └── click_on_digital_downloads()  # Navigate to products
│
├── 📝 registerPage.py           # Registration form handling
│   ├── fill_details()          # Complete registration form
│   ├── click_on_register()     # Submit registration
│   └── click_on_continue()     # Post-registration continue
│
├── 💿 digitalDownloadsPage.py  # Product catalog interactions
│   ├── click_on_random_item()  # Select random product
│   ├── get_title_from_item()   # Extract product title
│   ├── add_product_to_cart()   # Add to shopping cart
│   ├── click_on_shopping_cart()  # Navigate to cart
│   └── wait_for_adding_product()  # Wait for cart update
│
└── 🛒 shoppingCartPage.py      # Shopping cart operations
    └── get_the_product_on_cart()  # Retrieve cart items
```

### **Test Structure**
```
📁 tests/
├── 🧪 test_overall.py          # Main E2E test scenarios
│   └── test_register_and_add_item_to_shopping_cart()
│
├── 🔧 base_class.py             # Test base class with shared setup
│   ├── Page initialization
│   ├── Faker data generator
│   ├── Logger configuration
│   └── Page object instances
│
└── ⚙️ conftest.py               # Pytest configuration & fixtures
    ├── Browser setup/teardown
    ├── Viewport configuration
    ├── Screenshot on failure
    ├── Trace collection
    └── Allure attachments
```

### **Design Principles**
- **Single Responsibility Principle (SRP)**: Each page class handles specific UI section interactions
- **DRY (Don't Repeat Yourself)**: Common actions abstracted in BasePage
- **Encapsulation**: Private locators prevent direct access, forcing usage through methods
- **Maintainability**: Clear separation between test logic and page interactions
- **Scalability**: Easy extension with additional page objects and test scenarios
- **Testability**: Isolated components enable unit testing of page objects

---

## 🚀 Quick Start

### Prerequisites
Ensure you have the following installed:
- **Python 3.13.5+** ([Download](https://www.python.org/downloads/))
- **Docker & Docker Compose** ([Install Guide](https://docs.docker.com/get-docker/))
- **Git** ([Download](https://git-scm.com/downloads))

### 1️⃣ Clone Repository
```bash
git clone https://github.com/shlomi10/sunFlower.git
cd sunflower
```

### 2️⃣ Local Setup (Without Docker)
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install

# Run tests locally
pytest --alluredir=allure-results

# Generate and view Allure report
allure serve allure-results
```

### 3️⃣ Docker Execution (Recommended)
```bash
# Build and run complete test suite with reporting
docker-compose up

# Run tests in detached mode
docker-compose up -d

# View logs
docker-compose logs -f tests
```

### 4️⃣ Access Live Reports
After running tests with Docker Compose:

- **Allure UI Dashboard**: http://localhost:5050
- **Allure API Service**: http://localhost:5051
- **Full Report**: http://localhost:5051/allure-docker-service/projects/default/reports/latest/index.html

---

## 🛠️ Tech Stack

### **Core Testing Framework**
- **[Playwright](https://playwright.dev/)** `latest` - Modern browser automation
  - Auto-wait functionality for stable tests
  - Cross-browser support (Chromium, Firefox, WebKit)
  - Network interception and mocking
  - Built-in test isolation
  
- **[Python 3.13.5+](https://www.python.org/)** - Latest Python features
  - Type hints support for better code quality
  - Async/await capabilities
  - Enhanced error handling
  
- **[Pytest](https://pytest.org/)** `latest` - Advanced testing framework
  - Powerful fixtures and dependency injection
  - Parametrized testing support
  - Rich plugin ecosystem
  - Detailed test reporting

### **Test Enhancement & Utilities**
- **[Faker](https://faker.readthedocs.io/)** `latest` - Realistic test data generation
  - Names, emails, passwords, addresses
  - Locale-specific data
  - Custom providers support
  
- **[Allure Framework](https://docs.qameta.io/allure/)** `latest` - Enterprise test reporting
  - Rich visualizations and graphs
  - Historical test trends
  - Test categorization (Epic, Feature, Story)
  - Screenshot and video attachments
  - Step-by-step execution details
  
- **[pytest-playwright](https://playwright.dev/python/docs/test-runners)** - Seamless integration
  - Automatic browser lifecycle management
  - Built-in fixtures for pages and contexts
  - Parallel execution support
  
- **[pytest-rerunfailures](https://pypi.org/project/pytest-rerunfailures/)** - Flaky test handling
  - Automatic test retry on failure
  - Configurable retry attempts
  - Flaky test detection

### **DevOps & Infrastructure**
- **[Docker](https://www.docker.com/)** `latest` - Containerized execution
  - Consistent test environment across machines
  - Isolated dependencies
  - Version-locked browsers
  
- **[Docker Compose](https://docs.docker.com/compose/)** `latest` - Multi-service orchestration
  - Test + Allure service coordination
  - Volume management for reports
  - Network configuration
  
- **[Xvfb](https://www.x.org/releases/X11R7.6/doc/man/man1/Xvfb.1.xhtml)** - Virtual display server
  - Headless browser execution in Docker
  - Display buffer management
  - Screen resolution configuration

---

## 🧪 Test Execution Options

### **Local Development**
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_overall.py -v

# Run specific test method
pytest tests/test_overall.py::TestOverall::test_register_and_add_item_to_shopping_cart -v

# Run with detailed output and short traceback
pytest --tb=short --alluredir=allure-results -v

# Run with live logging
pytest --log-cli-level=INFO

# Generate and serve Allure report locally
allure serve allure-results
```

### **Headless vs Headed Execution**
```bash
# Run in headless mode (default in Docker)
pytest --headed=false

# Run in headed mode (visible browser)
pytest --headed=true

# Run with slow motion (debugging)
pytest --slowmo=1000
```

### **Browser Selection**
```bash
# Run with Chromium (default)
pytest --browser=chromium

# Run with Firefox
pytest --browser=firefox

# Run with WebKit
pytest --browser=webkit

# Run on all browsers
pytest --browser=chromium --browser=firefox --browser=webkit
```

### **Docker Execution Options**
```bash
# Run tests with default configuration
docker-compose up

# Run with custom pytest options
docker-compose run tests pytest tests/ -v --tb=short

# Run specific test in Docker
docker-compose run tests pytest tests/test_overall.py::TestOverall::test_register_and_add_item_to_shopping_cart

# Run in interactive mode (debugging)
docker-compose run tests bash
```

### **Parallel Execution (Advanced)**
```bash
# Install pytest-xdist
pip install pytest-xdist

# Run tests in parallel (4 workers)
pytest -n 4

# Run with auto-scaling to CPU count
pytest -n auto
```

---

## 📊 Test Reporting & Live Dashboard

### **Allure Report Features**
Our implementation provides enterprise-grade test reporting:

- **📈 Executive Dashboard**
  - Overall test execution statistics
  - Pass/Fail/Skip rate visualization
  - Test duration analysis
  - Historical trend graphs

- **📋 Detailed Test Steps**
  - Step-by-step execution flow with Allure decorators
  - Timing information for each step
  - Nested step hierarchies
  - Custom step descriptions

- **📸 Visual Evidence**
  - Automatic screenshots on test failures
  - Full-page screenshots for better context
  - Trace files for debugging (`trace.zip`)
  - Network activity logs

- **🎯 Test Organization**
  - Categorization by Epic, Feature, Story
  - Severity levels (Blocker, Critical, Normal, Minor, Trivial)
  - Custom tags and labels
  - Grouping by test suites

- **⏱️ Performance Metrics**
  - Test execution time breakdown
  - Slowest tests identification
  - Performance trends over time
  - Resource usage statistics

- **🔄 Flaky Test Detection**
  - Automatic retry with `@pytest.mark.flaky(reruns=1)`
  - Flaky test reporting
  - Success rate tracking

### **Accessing Reports**

#### **Local Execution**
```bash
# Generate and open report in browser
allure serve allure-results

# Generate static report
allure generate allure-results -o allure-report --clean

# Open generated report
allure open allure-report
```

#### **Docker Execution**
After running `docker-compose up`, access the following:

| Service | URL | Description |
|---------|-----|-------------|
| **Allure UI** | http://localhost:5050 | Interactive dashboard with project overview |
| **Allure API** | http://localhost:5051 | RESTful API for report data |
| **Latest Report** | http://localhost:5051/allure-docker-service/projects/default/reports/latest/index.html | Direct link to the latest test execution report |

#### **Report Persistence**
Reports are stored in the following volumes:
- `./allure-results/` - Raw test execution data
- `./allure-history/` - Historical trend data
- `./screenshots/` - Failure screenshots
- `./trace/` - Playwright trace files

### **Continuous Reporting in CI/CD**
Reports can be automatically published to:
- GitHub Pages
- AWS S3
- Azure Blob Storage
- Jenkins artifacts
- GitLab Pages

---

## 🔧 Configuration

### **Environment Variables** (`.env`)
Located in `utils/.env`:
```env
# Application Under Test
BASE_URL=https://demowebshop.tricentis.com/

# Browser Configuration (optional)
HEADLESS=true
BROWSER=chromium

# Timeout Settings (optional)
DEFAULT_TIMEOUT=30000
NAVIGATION_TIMEOUT=30000
```

### **Pytest Configuration** (`pytest.ini` or `conftest.py`)
Key configurations:
- **Automatic fixtures** for browser setup/teardown
- **Screenshot capture** on test failures (saved to `screenshots/`)
- **Trace collection** for debugging (saved to `trace/trace.zip`)
- **Flaky test handling** with automatic reruns (`@pytest.mark.flaky(reruns=1)`)
- **Allure decorators** for rich reporting

### **Browser Settings**
Configured in `conftest.py`:
```python
browser = playwright.chromium.launch(
    headless=headless_mode,
    args=["--no-sandbox", "--disable-dev-shm-usage"]
)
context = browser.new_context(no_viewport=True)
page = context.new_page()

# Maximize window for consistent element visibility
page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.availWidth, screen.availHeight);")
```

Features:
- **Maximized window** for consistent element visibility
- **No viewport restrictions** for responsive testing
- **Tracing enabled** for detailed debugging
- **Screenshot support** on failures
- **Automatic cleanup** after each test

### **Docker Configuration**
#### **Dockerfile**
- Base image: `python:3.11-slim`
- Includes Xvfb for headless execution
- Pre-installed Playwright browsers
- Optimized layer caching

#### **docker-compose.yml**
```yaml
services:
  tests:
    # Test execution service
    - Shared memory size: 1GB
    - Volume mounts for results
    - Environment variables

  allure:
    # Allure report service
    - Port 5051:5050
    - Result and history volumes

  allure-ui:
    # Allure UI dashboard
    - Port 5050:5252
    - Connects to allure service API
```

---

## 🐳 Docker Hub Image

### **Pre-built Image Available**
Pull and run the pre-built Docker image directly from Docker Hub:

```bash
# Pull the latest image
docker pull shlomi10/sunflower:latest

# Run tests directly
docker run --rm shlomi10/sunflower:latest

# Run with custom environment variables
docker run --rm -e BASE_URL=https://your-app.com shlomi10/sunflower:latest

# Run with volume mounts to access reports
docker run --rm \
  -v $(pwd)/allure-results:/app/allure-results \
  -v $(pwd)/screenshots:/app/screenshots \
  shlomi10/sunflower:latest
```

### **Docker Hub Repository**
🔗 **[hub.docker.com/r/shlomi10/sunflower](https://hub.docker.com/r/shlomi10/sunflower)**

### **Image Features**
- ✅ Python 3.13.5 with all dependencies pre-installed
- ✅ Playwright browsers (Chromium, Firefox, WebKit) included
- ✅ Xvfb configured for headless execution
- ✅ Optimized for CI/CD pipelines
- ✅ Regular updates with latest dependencies
- ✅ Multi-architecture support (amd64, arm64)

### **CI/CD Integration with Docker Hub**
```yaml
# Example GitHub Actions workflow
- name: Run tests from Docker Hub
  run: |
    docker pull shlomi10/sunflower:latest
    docker run --rm \
      -v ${{ github.workspace }}/allure-results:/app/allure-results \
      shlomi10/sunflower:latest
```

---

## 🧩 Key Components

### **BasePage Class** (`pages/basePage.py`)
Foundation for all page objects with reusable methods:

```python
class BasePage:
    # Navigation
    def navigate(url: str) -> None
    
    # Interactions
    def click(element: Locator) -> None
    def click_on_random_element(elements: Locator) -> None
    def type(element: Locator, text: str) -> None
    def fill(element: Locator, text: str) -> None
    
    # Information Retrieval
    def get_text(element: Locator) -> str
    def get_title_of_page() -> str
    def is_visible(element: Locator) -> bool
    
    # Waiting Strategies
    def wait_for_element_to_be_visible(element: Locator, timeout: int) -> None
    def wait_for_loader_to_disappear(element: Locator, timeout: int) -> None
    
    # Utilities
    def take_screenshot(path: str) -> None
    def switch_to_iframe(locator_str: str) -> FrameLocator
```

### **Test Data Generation**
Using Faker library for realistic test data:

```python
from faker import Faker

faker = Faker()

# Generate random user data
first_name = faker.first_name()  # "John"
last_name = faker.last_name()    # "Doe"
email = faker.email()            # "john.doe@example.com"
password = faker.password()      # "aB3$xYz9"
```

### **Allure Decorators**
Rich test documentation and reporting:

```python
@allure.epic("E-commerce Platform")
@allure.feature("User Management")
@allure.story("User Registration & Shopping Flow")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Validates end-to-end user journey from registration to cart")
def test_register_and_add_item_to_shopping_cart(self, initialize):
    with allure.step("Navigate to registration page"):
        # Test steps...
```

---

## 🏃‍♂️ CI/CD Integration

### **GitHub Actions Example**
Create `.github/workflows/tests.yml`:

```yaml
name: E2E Automation Tests

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]
  schedule:
    - cron: '0 2 * * *'  # Run daily at 2 AM

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Pull from Docker Hub
        run: docker pull shlomi10/sunflower:latest
      
      - name: Run tests
        run: |
          docker run --rm \
            -v ${{ github.workspace }}/allure-results:/app/allure-results \
            -v ${{ github.workspace }}/screenshots:/app/screenshots \
            shlomi10/sunflower:latest
      
      - name: Generate Allure Report
        if: always()
        uses: simple-elf/allure-report-action@master
        with:
          allure_results: allure-results
          allure_history: allure-history
      
      - name: Publish Report to GitHub Pages
        if: always()
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: allure-history
      
      - name: Upload Artifacts
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: test-results
          path: |
            allure-results/
            screenshots/
            trace/
          retention-days: 30
```

### **Jenkins Pipeline Example**
```groovy
pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/shlomi10/sunFlower.git'
            }
        }
        
        stage('Run Tests') {
            steps {
                sh 'docker-compose up --abort-on-container-exit'
            }
        }
        
        stage('Generate Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }
    
    post {
        always {
            archiveArtifacts artifacts: 'allure-results/**, screenshots/**, trace/**'
            cleanWs()
        }
    }
}
```

### **GitLab CI Example**
Create `.gitlab-ci.yml`:

```yaml
stages:
  - test
  - report

test:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker-compose up --abort-on-container-exit
  artifacts:
    when: always
    paths:
      - allure-results/
      - screenshots/
      - trace/
    expire_in: 30 days

report:
  stage: report
  image: frankescobar/allure-docker-service
  script:
    - allure generate allure-results -o allure-report
  artifacts:
    paths:
      - allure-report/
  only:
    - main
```

---

## 🛠 Debugging & Troubleshooting

### **Common Issues & Solutions**

#### **1. Browser Launch Failures**
```bash
# Error: Browser executable not found
# Solution: Install browser dependencies
python -m playwright install-deps
python -m playwright install
```

#### **2. Element Not Found**
```bash
# Error: Timeout waiting for element
# Solution 1: Increase timeout
pytest --timeout=60000

# Solution 2: Run with slower execution for debugging
pytest --slowmo=1000 --headed
```

#### **3. Docker Permission Issues**
```bash
# Error: Permission denied on volume mounts
# Solution: Fix directory permissions
sudo chown -R $USER:$USER ./allure-results ./screenshots ./trace

# Or run docker with current user
docker-compose run --user $(id -u):$(id -g) tests
```

#### **4. Port Already in Use**
```bash
# Error: Port 5050/5051 already allocated
# Solution: Stop conflicting services
docker-compose down
sudo lsof -ti:5050 | xargs kill -9
sudo lsof -ti:5051 | xargs kill -9
```

#### **5. Allure Report Not Generated**
```bash
# Check if results directory exists
ls -la allure-results/

# Manually generate report
allure generate allure-results -o allure-report --clean

# Check Docker logs
docker-compose logs allure
```

### **Debug Mode Execution**
```bash
# Enable verbose logging
pytest --log-cli-level=DEBUG -v

# Run with browser dev tools open
pytest --headed --slowmo=1000

# Enable Playwright debug mode
PWDEBUG=1 pytest tests/test_overall.py

# Run single test with full output
pytest tests/test_overall.py::TestOverall::test_register_and_add_item_to_shopping_cart -vv --tb=long
```

### **Analyzing Traces**
```bash
# Open trace in Playwright Inspector
playwright show-trace trace/trace.zip

# View in browser
python -m http.server 8000
# Navigate to http://localhost:8000 and upload trace.zip
```

---

## 📈 Performance & Reliability

### **Execution Speed Optimization**
- **Parallel execution** support with `pytest-xdist`
- **Browser context reuse** for faster test initialization
- **Smart waiting** with Playwright's auto-wait functionality (no manual `time.sleep()`)
- **Optimized locators** using CSS selectors for speed
- **Lazy loading** of page objects

### **Stability Features**
- **Flaky test handling** with automatic reruns (`@pytest.mark.flaky(reruns=1)`)
- **Robust element selection** with multiple locator strategies
- **Timeout management** with configurable wait times (default: 5000ms)
- **Error recovery** with detailed failure reporting and screenshots
- **Retry logic** for network-dependent operations
- **Explicit waits** for dynamic content (e.g., loading spinners)

### **Best Practices Implemented**
- ✅ No hardcoded waits (`time.sleep()`)
- ✅ Explicit waits for dynamic elements
- ✅ Page object locators as private class attributes
- ✅ Single assertion per test method
- ✅ Descriptive test and method names
- ✅ Test independence (no interdependencies)
- ✅ Cleanup in fixtures (teardown)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### **Development Workflow**
1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR_USERNAME/sunFlower.git`
3. **Create** feature branch: `git checkout -b feature/amazing-enhancement`
4. **Make** your changes following coding standards
5. **Add tests** for new functionality
6. **Ensure** all tests pass: `pytest`
7. **Commit** changes: `git commit -m "feat: add amazing enhancement"`
8. **Push** to branch: `git push origin feature/amazing-enhancement`
9. **Submit** pull request with detailed description

### **Coding Standards**
- Follow **PEP 8** Python style guide
- Use **type hints** for function parameters and return values
- Use **meaningful** variable and method names (e.g., `click_on_register()` not `click1()`)
- Add **Allure** decorators (`@allure.step`, `@allure.story`) for better reporting
- Include **docstrings** for classes and complex methods
- **Maintain** page object separation (no business logic in page classes)
- Keep **test methods focused** (single responsibility)

### **Pull Request Guidelines**
- **Title**: Use conventional commit format (e.g., `feat:`, `fix:`, `docs:`)
- **Description**: Clearly explain what and why
- **Tests**: Include tests for new features
- **Documentation**: Update README if needed
- **Screenshots**: Add before/after screenshots for UI changes

### **Code Review Process**
- At least 1 approval required
- All CI checks must pass
- No merge conflicts
- Code coverage maintained or improved

---

## 📚 Documentation & Resources

### **Official Documentation**
- [Playwright Python API Reference](https://playwright.dev/python/docs/api/class-playwright)
- [Pytest Official Documentation](https://docs.pytest.org/en/stable/)
- [Allure Framework Documentation](https://docs.qameta.io/allure/)
- [Docker Documentation](https://docs.docker.com/)

### **Learning Resources**
- [Page Object Model Best Practices](https://playwright.dev/docs/pom)
- [Playwright Testing Patterns & Best Practices](https://playwright.dev/docs/best-practices)
- [Python Testing with Pytest Book](https://pythontest.com/pytest-book/)
- [Allure Report Examples](https://demo.qameta.io/allure/)

### **Community & Support**
- [Playwright Discord](https://discord.com/invite/playwright)
- [Stack Overflow - Playwright Tag](https://stackoverflow.com/questions/tagged/playwright)
- [GitHub Issues](https://github.com/shlomi10/sunFlower/