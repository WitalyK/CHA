unit Unit1;

interface

uses
  Windows, Messages, SysUtils, Variants, Classes, Graphics, Controls, Forms,
  Dialogs, StdCtrls,ComObj;

type
  TForm1 = class(TForm)
    OpenDialog1: TOpenDialog;
    Button1: TButton;
    Label1: TLabel;
    procedure EFEX;
    procedure FormCreate(Sender: TObject);
    procedure Button1Click(Sender: TObject);
    function LastPos(SubStr, S: string): Integer;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

var
  Form1: TForm1;
  rekl,rek, playlist, vyvod,pley,efir,vvodx : textfile;
  i,t,k,p,time1,time2,timed,a1,b1,c1,d1,e1,g1,abs1,abc1,s,ib,ix,tx,cx,rx,mx,t1,sss,ss1 : integer;
  block,blockv, blockt,blockr: array[0..100] of string [255];
  savedTitle,NumbeRek,FName1,FName2,FName3,name1,name2,name3,name4,name5,str1,kon1,nac1,b1s,c1s,d1s,bds,tempname,asd1,namer,FName1x,FName2x,name1x: string;
  Excel, Cell2, Cell1: Variant;
  timeblock: array[0..100] of integer;
  hronoblock: array[0..100] of integer;
  PrRek: boolean;

implementation

{$R *.dfm}


procedure TForm1.FormCreate(Sender: TObject);
begin
EFEX;
end;

// ������ �����

procedure TForm1.EFEX;
begin
  if OpenDialog1.Execute then
  begin
  FName1x:=OpenDialog1.FileName;
      AssignFile (vvodx, FName1x);
    Reset(vvodx);
    Excel := CreateOleObject('Excel.Application');
Excel.WorkBooks.Add;

delete(Fname1x,pos('.air',Fname1x),5);
FName2x:=FName1x;
delete(FName2x,1,Length(Fname2x)-10);
delete(Fname1x,LastPos('\',Fname1x)+1,Length(Fname1x));
Fname1x:=Fname1x+'������ ����������� ������� �� '+Fname2x;

ix:=2;
      Excel.columns[1].NumberFormat := '';
      Excel.columns[1].ColumnWidth := 12.29;
      Excel.columns[2].ColumnWidth := 62.71;
      Excel.columns[3].ColumnWidth := 10;
      Excel.columns[4].ColumnWidth := 22;
      Excel.columns[5].ColumnWidth := 18;
      Excel.columns[6].ColumnWidth := 19;
      Excel.columns[7].ColumnWidth := 24;
      Excel.columns[8].ColumnWidth := 30;
      Excel.columns[9].ColumnWidth := 23;
      Excel.rows['1'].Font.Bold := 1;
      Excel.rows ['1'].rowheight:=45;
      Excel.rows['1'].Font.size := 36;
      Excel.rows['1'].Font.Name := 'Calibri';
      Excel.Range['A1', 'I1'].Merge;
      Excel.Cells[1, 1].Value:=Fname2x;
      Excel.rows['2'].Interior.ColorIndex := 15;
      Excel.rows['2'].WrapText:=true;
      Excel.rows['2'].Font.Bold := 1;
      Excel.rows ['2'].rowheight:=55;
      Excel.rows['2'].Font.size := 15;
      Excel.rows['2'].Font.Name := 'Calibri';
      Excel.rows['2'].NumberFormat := '@';

      Excel.Cells[ix, 1].Value:='����� ������ � ����';
      Excel.Cells[ix, 2].Value:='�������� ��������';
      Excel.Cells[ix, 3].Value:='����. ���';
      Excel.Cells[ix, 5].Value:='����������� �������';
      Excel.Cells[ix, 6].Value:='����������� �������';
      Excel.Cells[ix, 7].Value:='�����/������� ��������';
      Excel.Cells[ix, 8].Value:='���� ��������';
      Excel.Cells[ix, 9].Value:='��������� ��������';
      ix:=ix+1;
      tx:=0;
      cx:=0;
      PrRek:=false;
      repeat
      readln (vvodx,name1x);
      until pos ('wait time',name1x)>0;

      Excel.Cells[ix, 2].Value:='�������� ������� '+copy (name1x,11,7);
      Excel.rows [ix].rowheight:=30;
      Excel.rows[ix].Font.Bold := 1;
      Excel.Cells[ix+1, 1].Value:=copy (name1x,11,7);
      Excel.rows [ix].rowheight:=30;
      Excel.rows[ix].Font.Bold := 1;
      ix:=ix+1;
      repeat
      readln (vvodx,name1x);
      if name1x='' then tx:=tx+1 else tx:=0;

      if pos ('logoOn',name1x)>0 then
      begin
      Excel.Cells[ix, 2].Value:='����';
            Excel.rows [ix].rowheight:=30;
      Excel.rows[ix].Font.Bold := 1;
      ix:=ix+1;
      end;

      if pos ('wait time',name1x)>0 then
      begin
      Excel.Cells[ix, 2].Value:='��������� ������� '+copy (name1x,11,7);
      Excel.Cells[ix+1, 1].Value:=copy (name1x,11,7);

      Excel.Cells[ix, 6].Value:='=A'+inttostr(ix+1)+'-A'+inttostr(ix-1);
       Excel.Cells[ix, 6].Font.ColorIndex:=3;
            Excel.rows [ix].rowheight:=30;
      Excel.rows[ix].Font.Bold := 1;
      ix:=ix+1;
      end;


      if pos ('movie',name1x)>0
      then
      begin
      if cx<>28 then
      begin
             Excel.rows [ix].rowheight:=30;
            Excel.rows[ix].Font.Bold := 1;
       end;
      Excel.rows[ix].Interior.ColorIndex :=cx;
//      Excel.Cells[ix, 6].Value:=copy(name1x,pos(':\',name1x)-2,100);
      Excel.Cells[ix+1, 1].Value:='=A'+inttostr(ix)+'+F'+inttostr(ix);

      if pos('<',name1x)>0 then
      begin
//      Excel.Cells[ix, 4].Value:=copy (name1x,8,10);
      Excel.Cells[ix, 6].Value:=copy (name1x,20,10);
      end
      else
      begin
//      Excel.Cells[ix, 4].Value:='';
      Excel.Cells[ix, 6].Value:=copy (name1x,7,10);
      end;
      repeat
      delete (name1x,1,pos('\',name1x));
      until pos('\',name1x)<1;
if  pos('-3',name1x)>0 then delete (name1x,1,3);
delete (name1x,pos('.avi',name1x),5);
delete (name1x,pos('.mpg',name1x),5);
delete (name1x,pos('.mpeg',name1x),5);

      Excel.Cells[ix, 2].Value:=name1x;
      ix:=ix+1;
      end;


      if pos ('video',name1x)>0
      then
      begin
            if cx<>28 then
      begin
             Excel.rows [ix].rowheight:=30;
            Excel.rows[ix].Font.Bold := 1;
       end;
         Excel.rows[ix].Interior.ColorIndex := 4;
//      Excel.Cells[ix, 6].Value:='����������';
      Excel.Cells[ix, 2].Value:='������ ����';
//      Excel.Cells[ix, 4].Value:='';
      Excel.Cells[ix, 6].Value:=copy(name1x,8,7);
      Excel.Cells[ix+1, 1].Value:='=A'+inttostr(ix)+'+F'+inttostr(ix);
      ix:=ix+1;
      end;


      if pos ('��������� ����',name1x)>0 then
      begin
        if pos ('������',name1x)>0 then
        begin
          if not PrRek then
          begin
            cx:=28;
            rx:=ix;
            PrRek:=true;
            NumbeRek:=copy(name1x,26,3);
          end
          else
          begin
            savedTitle := Application.Title;
            try
              Application.Title := '��-��, �������� ���!';
              ShowMessage('��������!!! ��� ����� ���������� ����� '+NumbeRek+#13#10+'����������� ��������!');
            finally
              Application.Title := savedTitle;
            end;
            Excel.DisplayAlerts := False;
            Excel.Quit;
            exit;
          end;
        end;
        Excel.rows[ix].Font.ColorIndex := 3;
        Excel.rows[ix].Interior.ColorIndex := cx;
//        Excel.Cells[ix, 6].Value:='';
        Excel.Cells[ix, 2].Value:=copy(name1x,10,100);
//      Excel.Cells[ix, 4].Value:='';
        Excel.Cells[ix, 6].Value:='';
        Excel.Cells[ix+1, 1].Value:='=A'+inttostr(ix)+'+F'+inttostr(ix);
        if pos ('�����',name1x)>0 then
        begin
          if PrRek then
          begin
            cx:=0;
            Excel.Cells[rx, 5].Value:='=A'+inttostr(ix)+'-A'+inttostr(rx);
            PrRek:=false;
          end
          else
          begin
            savedTitle := Application.Title;
            try
              Application.Title := '��, �������� �����!';
              ShowMessage('��������!!! ��� ������ ���������� ����� '+copy(name1x,26,3)+#13#10+'����������� ��������!');
            finally
              Application.Title := savedTitle;
            end;
            Excel.DisplayAlerts := False;
            Excel.Quit;
            exit;
          end;
        end;
        ix:=ix+1;
      end;
      until tx=3;
Cell2:=Excel.Cells[ix, 9];
Excel.Range['A2', Cell2].Select;
Excel.Selection.Borders.LineStyle := 1; // ����� ����� ��������
Excel.Selection.Borders.Weight := 1;// ������� �����
Cell1:=Excel.Cells[ix+4, 1];
Cell2:=Excel.Cells[ix+4, 9];
Excel.Range[Cell1, Cell2].Merge;
Excel.Cells[ix+4, 1].Font.size := 14;
Excel.Cells[ix+4, 1].Value:='����������� �������� ________________________________/_______________________________/';
Excel.Range['A1:E1000'].Select;
Excel.Selection.HorizontalAlignment:=3;
Excel.Selection.NumberFormat := '��:��:��,00';
Excel.Range['B1:D1000'].Select;
Excel.Selection.HorizontalAlignment:=3;
Excel.columns[2].HorizontalAlignment:=4;
Excel.rows[2].HorizontalAlignment:=3;
Excel.rows[2].VerticalAlignment:=2;
Excel.Range['A1:A1'].Select;
Excel.ActiveWindow.SplitRow := 2;
Excel.ActiveWindow.FreezePanes := 1;
Excel.ActiveWorkbook.SaveAs(FName1x+'.xlsx');
Excel.Quit;
close;
end;
end;

procedure TForm1.Button1Click(Sender: TObject);
begin
form1.Close;
end;

function TForm1.LastPos(SubStr, S: string): Integer;
var
  Found, Len, Pos: integer;
begin
  Pos := Length(S);
  Len := Length(SubStr);
  Found := 0;
  while (Pos > 0) and (Found = 0) do
  begin
    if Copy(S, Pos, Len) = SubStr then
      Found := Pos;
    Dec(Pos);
  end;
  LastPos := Found;
end;


end.
