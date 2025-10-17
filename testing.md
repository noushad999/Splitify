# Splitify Automation Testing

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://www.selenium.dev/)
[![Test Status](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


> Complete end-to-end automated testing suite for Splitify expense management application using Selenium WebDriver.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Test Coverage](#test-coverage)
- [Test Results](#test-results)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project provides comprehensive automated testing for the Splitify web application, covering the complete user journey from authentication through expense creation, group management, and settlement recording.

**Application URL:** `http://localhost:3000`  
**Test Framework:** Selenium WebDriver with Python  
**Total Test Steps:** 41  
**Success Rate:** 100%

## ✨ Features

- ✅ **Complete User Journey Testing** - Sign-in to settlement recording
- ✅ **Clerk Authentication Integration** - Automated login with test accounts
- ✅ **Individual Expense Management** - Create and manage personal expenses
- ✅ **Group Management** - Create groups and add members
- ✅ **Group Expense Creation** - Manage shared expenses
- ✅ **Settlement Recording** - Track and record settlements
- ✅ **Robust Error Handling** - Multiple fallback strategies
- ✅ **Comprehensive Logging** - Detailed execution logs
- ✅ **Screenshot on Failure** - Automatic debugging screenshots

## 📦 Prerequisites

Before running the tests, ensure you have the following installed:

- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Chrome Browser** - Latest version
- **ChromeDriver** - Matching your Chrome version
- **Git** - For cloning the repository

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/splitify-automation.git
cd splitify-automation
```

### 2. Install Python Dependencies

```bash
pip install selenium
```

### 3. Download ChromeDriver

Download ChromeDriver matching your Chrome version from [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)

Place `chromedriver.exe` in the project root directory:

```
splitify-automation/
├── chromedriver.exe
├── main.py
└── README.md
```

## ⚙️ Configuration

### Test Credentials

The automation uses Clerk test mode credentials:

```python
TEST_EMAIL = "clerk.test+automation@example.com"
TEST_PASSWORD = "test@splitify1"
```

**Note:** For production testing, update credentials in the script.

### Application URL

Update the application URL in `main.py` if different:

```python
driver.get("http://localhost:3000")  # Change port if needed
```

## 🎮 Usage

### Run the Complete Test Suite

```bash
python main.py
```

### Expected Output

```
======================================================================
🚀 STARTING SPLITIFY COMPLETE AUTOMATION TEST
======================================================================

INFO: Navigating to Splitify...
INFO: Step 1: Clicking sign-in button...
INFO: ✓ Sign-in button clicked
...
[41 steps execute]
...

======================================================================
✅ AUTOMATION COMPLETED SUCCESSFULLY!
======================================================================
✓ Signed in successfully
✓ Created individual expense: dinner - 6000
✓ Viewed settlement tab
✓ Created group: testing_group
✓ Added members: noushad ramim, md noushad
✓ Created group expense: food - 10000
✓ Recorded settlement: 1000
Final URL: http://localhost:3000/dashboard
======================================================================

✅ Test PASSED
```

## 🧪 Test Coverage

### Phase 1: Authentication (Steps 1-6)

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC_AUTH_001 | User sign-in with Clerk | ✅ Pass |
| TC_AUTH_002 | Email validation | ✅ Pass |
| TC_AUTH_003 | Password authentication | ✅ Pass |
| TC_AUTH_004 | Dashboard navigation | ✅ Pass |

### Phase 2: Individual Expense (Steps 7-16)

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC_EXP_001 | Create individual expense | ✅ Pass |
| TC_EXP_002 | Add participant | ✅ Pass |
| TC_EXP_003 | Set paid by option | ✅ Pass |

### Phase 3: Group Management (Steps 18-27)

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC_GRP_001 | Create new group | ✅ Pass |
| TC_GRP_002 | Add multiple members | ✅ Pass |

### Phase 4: Group Expense (Steps 28-36)

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC_GEXP_001 | Create group expense | ✅ Pass |
| TC_GEXP_002 | Select group | ✅ Pass |

### Phase 5: Settlement (Steps 37-41)

| Test Case | Description | Status |
|-----------|-------------|--------|
| TC_SET_001 | Record settlement | ✅ Pass |
| TC_SET_002 | Enter settlement amount | ✅ Pass |

## 📊 Test Results

### Summary Statistics

- **Total Steps:** 41
- **Passed:** 41 (100%)
- **Failed:** 0 (0%)
- **Execution Time:** ~120-150 seconds
- **Browser:** Chrome (Latest)
- **Status:** ✅ All Tests Passing

### Test Data Used

| Field | Value |
|-------|-------|
| Individual Expense | dinner - 6000 |
| Group Name | testing_group |
| Group Members | noushad ramim, md noushad |
| Group Expense | food - 10000 |
| Settlement Amount | 1000 |

## 📁 Project Structure

```
splitify-automation/
│
├── main.py                 # Main automation script
├── chromedriver.exe        # Chrome WebDriver executable
├── README.md              # This file
├── error_screenshot.png   # Auto-generated on failure
└── requirements.txt       # Python dependencies (optional)
```

## 🛠️ Troubleshooting

### Common Issues

#### 1. ChromeDriver Version Mismatch

**Error:** `SessionNotCreatedException`

**Solution:**
```bash
# Check Chrome version
chrome --version

# Download matching ChromeDriver from:
# https://chromedriver.chromium.org/downloads
```

#### 2. Element Not Found

**Error:** `TimeoutException: Element not found`

**Solution:**
- Check if application is running on `http://localhost:3000`
- Verify XPath selectors match current application version
- Check `error_screenshot.png` for visual debugging

#### 3. Authentication Failure

**Error:** `Invalid credentials`

**Solution:**
- Ensure Clerk test mode is enabled
- Verify test email format: `clerk.test+automation@example.com`
- Check password: `test@splitify1`

### Debug Mode

Enable detailed logging by checking the console output. The script automatically logs each step with timestamps.

## 🔧 Advanced Configuration

### Custom Wait Times

Modify wait times in the script:

```python
wait = WebDriverWait(driver, 20)  # Standard wait
extended_wait = WebDriverWait(driver, 30)  # Extended wait
```

### Headless Mode

Run tests without GUI:

```python
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
```

### Custom Screenshot Path

```python
driver.save_screenshot("custom/path/screenshot.png")
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Code Style

- Follow PEP 8 guidelines
- Add comments for complex logic
- Update README for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Md Noushad Jahan Ramim** - *Initial work* - [GitHub Profile](https://github.com/noushad999)

## 🙏 Acknowledgments

- Selenium WebDriver team
- Clerk authentication platform
- Splitify development team

## 📞 Support

For issues and questions:

- **GitHub Issues:** [Create an issue](https://github.com/yourusername/splitify-automation/issues)
- **Email:** your.email@example.com
- **Documentation:** [Wiki](https://github.com/yourusername/splitify-automation/wiki)

## 📈 Future Enhancements

- [ ] Add pytest integration
- [ ] Implement Page Object Model (POM)
- [ ] Add parallel test execution
- [ ] Create CI/CD pipeline (GitHub Actions)
- [ ] Add test report generation (Allure/HTML)
- [ ] Implement data-driven testing
- [ ] Add API testing integration
- [ ] Create Docker container for tests

***

**⭐ If you find this project helpful, please give it a star!**

**Last Updated:** October 18, 2025  
**Version:** 1.0.0

[1](https://github.com/Umutayb/test-automation-template)
[2](https://github.com/testmoapp/example-selenium-test-automation-reporting)
[3](https://gist.github.com/mklabs/98a3badabcdef902618e0a59a935b597)
[4](https://github.com/topics/automation-testing)
[5](https://github.com/ctrf-io/github-test-reporter)
[6](https://www.testmo.com/guides/github-actions-test-automation/)
[7](https://www.frugaltesting.com/blog/github-test-case-management-and-testing-automation-integration)
[8](https://github.com/marketplace/actions/test-reporting)
[9](https://allurereport.org)
