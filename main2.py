# 必要なライブラリをインポート
import streamlit as st
import numpy as np
import pandas as pd

# タイトルとテキストを記入
st.title('Streamlit 基礎')
st.write('Hello World!')

# エラーについて
# 実施したこと　
# ・Windowsの「環境設定を編集」で「path」をStreamlit.exeが配置されているフォルダにした
# ・Visual Studio Codeに「Python」を拡張機能からインストールした⇒「エラーが指定されてモジュールが見つかりません」に変わる
# (・anaconda prompt でStreamlit 、Numpy、pandasをインストール)
# ・Visual Studio Codeの設定でPython: Conda Path とPython: Default Interpreter Path　をともに「 C:\Users\capri\anaconda3」に設定
# (下記URLの手順に従った時に、環境構築をしたときの場所に変更)
# ・anaconda powershell promptでNumpyをアンインストール後、再インストール
# https://python0to1.com/499/ の手順にしたがって環境構築を行った
# ・エラーはでなくなったが、何も表示されない。 
# streamlit run C:\Users\capri\Desktop\Streamlit\main.py　とパスに変えても何も表示されない
# https://qiita.com/sho73movie/items/fa5212fe41382d4dfb6f
# 上記リンクの手順に従ってPython › Analysis: Extra Pathsの設定追加


# 質問
# 
# streamlit : 用語 'streamlit' は、コマンドレット、関数、スクリプト ファイル、または操作可能なプログラムの名前として認識され
# ません。名前が正しく記述されていることを確認し、パスが含まれている場合はそのパスが正しいことを確認してから、再試行してください。
# Windowsの「環境設定を編集」で「path」を編集⇒新規
# 「streamlit.exe」が配置されているフォルダを指定⇒治らず
# VS Code 内で Anaconda を使えるように Path を通す
# 左上の三本線からファイル→ユーザー設定→設定で「python」と検索
# pythonが出てこず、インストールされていなかったようなので、
# 拡張機能からインストール
# エラーが「指定されたモジュールが見つかりません。」に変わる
# もう一度設定でpython：pythonpathと検索し、「python.exe」
# がある場所を指定⇒エラー
# anaconda prompt でStreamlit 、Numpy、pandasをインストール
# ↑今まではanaconda powershell promptの方でしてしまっていた
#　⇒エラー：指定されたモジュールが見つかりません。
# Python: Conda Path とPython: Default Interpreter Path　をともに「C:\Users\capri\anaconda3\python.exe」に設定
# ⇒エラー：指定されたモジュールが見つかりません。
# numpyをアンインストールして再インストール⇒エラー：指定されたモジュールが見つかりません。
