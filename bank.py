if balance > average_balance
    

    if above_average_accounts:
        for name, balance in above_average_accounts.items():
            print(f"**حساب:** {name} | موجودی: {balance:,.0f} ریال")
    else:
        print("هیچ حسابی موجودی بالاتر از میانگین ندارد.")
    print("=======================================================")


def run_bank_simulation():
    """
    تابع اصلی برای اجرای شبیه‌سازی بانک.
    """
    accounts = {}  # دیکشنری برای ذخیره حساب‌ها: {نام_صاحب: موجودی}

    print(" خوش آمدید به سیستم شبیه‌سازی بانک.")

    # 1. گرفتن تعداد حساب‌ها
    while True:
        try:
            num_accounts = int(input("چند حساب بانکی می‌خواهید ایجاد کنید؟ (به عدد): "))
            if num_accounts >= 1:
                break
            else:
                print("لطفاً یک عدد صحیح مثبت وارد کنید.")
        except ValueError:
            print("ورودی نامعتبر است. لطفاً یک عدد صحیح وارد کنید.")

    # 2. ایجاد حساب‌ها
    for i in range(num_accounts):
        print(f"\n--- ایجاد حساب شماره {i + 1} از {num_accounts} ---")
        accounts = create_account(accounts)
    
    # 3. منوی عملیات
    while True:
        print("\n" + "="*30)
        print("=====  منوی عملیات بانکی =====")
        print("1. نمایش موجودی همه حساب‌ها")
        print("2. سپرده‌گذاری در حساب")
        print("3. برداشت از حساب")
        print("4. نمایش حساب‌هایی با موجودی بیشتر از میانگین")
        print("5. خروج از برنامه")
        print("="*30)

        choice = input("لطفاً شماره گزینه مورد نظر را وارد کنید: ").strip()

        if choice == '1':
            display_all_balances(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            display_above_average(accounts)
        elif choice == '5':
            print("\n با تشکر از استفاده شما. برنامه خاتمه یافت.")
            break
        else:
            print(" ورودی نامعتبر. لطفاً یک عدد بین 1 تا 5 وارد کنید.")

# اجرای برنامه
run_bank_simulation()