import os
import pandas as pd
import math

def process(n_1: float = 0.0, n_2: float = 0.0, angle: int = 0, path: tuple[str] | None = None):
    def dp(wave_number_series, n_1, n_2, angle):
        angle_rad = math.radians(angle)
        sin_angle_sq = math.sin(angle_rad)**2
        n_ratio_sq = (n_2 / n_1)**2
    
        if sin_angle_sq <= n_ratio_sq:
            return float('nan')
        
        denominator = 2 * math.pi * n_1 * math.sqrt(sin_angle_sq - n_ratio_sq)
        wavelength_um = 10000 / wave_number_series
        return wavelength_um / denominator

    if path is None:
        import tkinter.filedialog as tkfd
        filetypes = [
            ("text File", "*.txt"),
            ("csv File", "*.csv *.CSV"),
            ("other File", "*")
        ]
        
        path = tkfd.askopenfilenames(filetypes=filetypes)
        
    if not path:
        print("ファイル選択がキャンセルされました。")
        return

    for col in path:
        ext = os.path.splitext(col)
        
        
        if ext[1].lower() == ".txt":
            dd = pd.read_csv(col, sep=r"\s+", skiprows=1, header=None, names=["Wave_number", "Absorbance"])
        elif ext[1].lower() == ".csv":
            dd = pd.read_csv(col)
        else:
            print(f"Skipped unsupported file: {col}")
            continue
        
        try:
            # 補正計算
            dd['Penetration_Depth_um'] = dp(dd['Wave_number'], n_1, n_2, angle)
            dp_min = dd['Penetration_Depth_um'].min()
            dd['Corrected_Abs'] = dd['Absorbance'] / (dd['Penetration_Depth_um'] / dp_min)
            
            
            dir_name = os.path.dirname(col)
            file_base, _ = os.path.splitext(os.path.basename(col))
            out_path = os.path.join(dir_name, f"ATRcorr_{file_base}.csv")
            
            dd.to_csv(out_path, index=False)
            print(f"Saved: {out_path}")
            
        except KeyError as e:
            print(f"Error in {col}: 列名 {e} が見つかりません。")

process(n_1 = 2.39, n_2 = 1.50, angle = 45)