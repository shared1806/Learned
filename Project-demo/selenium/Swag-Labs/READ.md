<!-- with open('report.txt', 'w') as f:
    runner = unittest.TextTestRunner(stream=f, verbosity=2)
    result = runner.run(suite) -->

project/
│
├── test/
│   ├── test_cases/
│   │   ├── login_tests/
│   │   │   ├── TC001_Login_Success.xlsx
│   │   │   ├── TC002_Login_Failure.xlsx
│   │   │   └── ...
│   │   ├── order_tests/
│   │   │   ├── TC003_Order_Success.xlsx
│   │   │   ├── TC004_Order_Failure.xlsx
│   │   │   └── ...
│   │   └── ...
│   │
│   ├── test_scripts/
│   │   ├── login_test.py
│   │   ├── order_test.py
│   │   └── ...
│   │
│   ├── test_data/
│   │   ├── login_data.json
│   │   ├── order_data.json
│   │   └── ...
│   │
│   ├── results/
│   │   ├── report.html
│   │   ├── TC001_Login_Success_Result.txt
│   │   └── ...
│   │
│   ├── utils/
│   │   ├── config.py
│   │   ├── selenium_utils.py
│   │   └── ...
│   └── README.md
│
└── main.py