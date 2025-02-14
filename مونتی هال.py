import random  

def monty_hall(simulations=1000):  
    win_with_switch = 0  

    for _ in range(simulations):  
        doors = [0, 0, 1]  # دو بز (0) و یک جایزه (1)  
        random.shuffle(doors)  # درها را به‌صورت تصادفی جابجا می‌کنیم  

        choice = random.randint(0, 2)  # بازیکن یکی از سه در را انتخاب می‌کند  
        del doors[choice]  # در انتخابی بازیکن را حذف می‌کنیم  

        doors.remove(0)  # مجری یکی از درهای بز را حذف می‌کند  

        if doors[0] == 1:  # اگر تنها در باقی‌مانده جایزه داشته باشد  
            win_with_switch += 1  

    return win_with_switch / simulations  # درصد برد در صورت تغییر انتخاب  

print(monty_hall())  # اجرای شبیه‌سازی و نمایش نتیجه  
