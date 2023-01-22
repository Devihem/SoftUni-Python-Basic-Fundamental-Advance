progress_input = int(input())
divised_by_10 = int(progress_input/10)
symbol_1 = "%"
symbol_2 = "."
if progress_input == 100:
    print("100% Complete!\n[%%%%%%%%%%]")
else:
    print(f"{progress_input}% [{divised_by_10*symbol_1}{(10-divised_by_10)*symbol_2}]\nStill loading...")
