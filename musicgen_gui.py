import tkinter as tk
from tkinter import messagebox
from audiocraft.models import MusicGen
import torch

def generate_music():
    model_type = model_var.get()
    prompt_text = prompt_entry.get("1.0", tk.END).strip()
    max_duration = int(duration_entry.get())
    output_file = output_entry.get()

    if not prompt_text:
        messagebox.showerror("Error", "プロンプトが入力されていません。")
        return

    if not output_file:
        messagebox.showerror("Error", "出力ファイル名が入力されていません。")
        return

    # モデルのロード
    model = MusicGen.get_pretrained(model_type)

    # 音楽生成
    output = model.generate([prompt_text], max_duration=max_duration)
    
    # 音楽の保存
    model.save_wavs(output, output_file)
    messagebox.showinfo("完了", f"音楽が生成され、{output_file} に保存されました。")

# GUIのセットアップ
root = tk.Tk()
root.title("MusicGen GUI")

# モデル選択
tk.Label(root, text="モデルの選択:").grid(row=0, column=0, sticky="w")
model_var = tk.StringVar(value="small")
model_options = ["small", "medium", "large", "melody"]
model_menu = tk.OptionMenu(root, model_var, *model_options)
model_menu.grid(row=0, column=1, sticky="w")

# プロンプト入力
tk.Label(root, text="プロンプト:").grid(row=1, column=0, sticky="nw")
prompt_entry = tk.Text(root, height=5, width=40)
prompt_entry.grid(row=1, column=1, sticky="w")

# 生成する音楽の長さ（秒）
tk.Label(root, text="音楽の長さ (秒):").grid(row=2, column=0, sticky="w")
duration_entry = tk.Entry(root)
duration_entry.insert(0, "30")
duration_entry.grid(row=2, column=1, sticky="w")

# 出力ファイル名
tk.Label(root, text="出力ファイル名:").grid(row=3, column=0, sticky="w")
output_entry = tk.Entry(root)
output_entry.insert(0, "generated_music.wav")
output_entry.grid(row=3, column=1, sticky="w")

# 生成ボタン
generate_button = tk.Button(root, text="生成", command=generate_music, width=20, height=2, bg="green", fg="white")
generate_button.grid(row=4, columnspan=2, pady=10)

# GUIの開始
root.mainloop()
