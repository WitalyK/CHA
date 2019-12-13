object Form1: TForm1
  Left = 310
  Top = 130
  Width = 243
  Height = 102
  Caption = #1050#1086#1085#1074#1077#1088#1090#1077#1088
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 16
    Top = 8
    Width = 103
    Height = 38
    Caption = #1043#1086#1090#1086#1074#1086
    Font.Charset = DEFAULT_CHARSET
    Font.Color = clWindowText
    Font.Height = -27
    Font.Name = 'Arial Black'
    Font.Style = []
    ParentFont = False
  end
  object Button1: TButton
    Left = 128
    Top = 8
    Width = 81
    Height = 41
    Caption = #1042#1099#1093#1086#1076
    TabOrder = 0
    OnClick = Button1Click
  end
  object OpenDialog1: TOpenDialog
    Filter = '(*.air)|*.air'
    InitialDir = 'D:\Reklama\'#1074' '#1101#1092#1080#1088
    Title = #1042#1099#1073#1088#1072#1090#1100' '#1096#1072#1073#1083#1086#1085'  '#1088#1077#1082#1083#1072#1084#1099
    Left = 16
    Top = 32
  end
end
