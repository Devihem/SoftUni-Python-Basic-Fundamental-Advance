progress_input = int(input()) // 10
symbol_1, symbol_2 = "%", "."
if progress_input == 10:
    print("100% Complete!\n[%%%%%%%%%%]")
else:
    print(f"{progress_input * 10}% [{progress_input * symbol_1}{(10-progress_input) * symbol_2}]\nStill loading...")
