import PySimpleGUI as sg
import fb_stat as fbs

labelsColumn = sg.Column([
	[sg.Text("Forwards")],
	[sg.Text("Player Stats")],
	[sg.Text("Player Tier")],
	[sg.Text("")],
	[sg.Text("Midfielders")],
	[sg.Text("Player Stats")],
	[sg.Text("Player Tier")],
	[sg.Text("")],
	[sg.Text("Defenders")],
	[sg.Text("Player Stats")],
	[sg.Text("Player Tier")],
	[sg.Text("")]])

column1 = sg.Column([
	[sg.Text("xG Per90")],
	[sg.In(key='-fps1-',size = (10, 1))],
	[sg.In(key='-fpt1-',size = (10, 1))],
	[sg.Text("",key="-result11-")],
	[sg.Text("KeyP Per90",size = (10, 1))],
	[sg.In(key='-mps1-',size = (10, 1))],
	[sg.In(key='-mpt1-',size = (10, 1))],
	[sg.Text("",key="-result12-")],
	[sg.Text("Tackles Per90")],
	[sg.In(key='-dps1-',size = (10, 1))],
	[sg.In(key='-dpt1-',size = (10, 1))],
	[sg.Text("",key="-result13-")]])

column2 = sg.Column([
	[sg.Text("Shots Per90")],
	[sg.In(key='-fps2-',size = (10, 1))],
	[sg.In(key='-fpt2-',size = (10, 1))],
	[sg.Text("",key="-result21-")],
	[sg.Text("PassSuc %",size = (10, 1))],
	[sg.In(key='-mps2-',size = (10, 1))],
	[sg.In(key='-mpt2-',size = (10, 1))],
	[sg.Text("",key="-result22-")],
	[sg.Text("Inter Per90")],
	[sg.In(key='-dps2-',size = (10, 1))],
	[sg.In(key='-dpt2-',size = (10, 1))],
	[sg.Text("",key="-result23-")]])
	
column3 = sg.Column([
	[sg.Text("KeyP Per90")],
	[sg.In(key='-fps3-',size = (10, 1))],
	[sg.In(key='-fpt3-',size = (10, 1))],
	[sg.Text("",key="-result31-")],
	[sg.Text("Dribbles Per90",size = (10, 1))],
	[sg.In(key='-mps3-',size = (10, 1))],
	[sg.In(key='-mpt3-',size = (10, 1))],
	[sg.Text("",key="-result32-")],
	[sg.Text("DribbledP Per90")],
	[sg.In(key='-dps3-',size = (10, 1))],
	[sg.In(key='-dpt3-',size = (10, 1))],
	[sg.Text("",key="-result33-")]])
	
column4 = sg.Column([
	[sg.Text("Dribbles Per90")],
	[sg.In(key='-fps4-',size = (10, 1))],
	[sg.In(key='-fpt4-',size = (10, 1))],
	[sg.Text("",key="-result41-")],
	[sg.Text("Disp Per90",size = (10, 1))],
	[sg.In(key='-mps4-',size = (10, 1))],
	[sg.In(key='-mpt4-',size = (10, 1))],
	[sg.Text("",key="-result42-")],
	[sg.Text("LongB Per90")],
	[sg.In(key='-dps4-',size = (10, 1))],
	[sg.In(key='-dpt4-',size = (10, 1))],
	[sg.Text("",key="-result43-")]])

column5 = sg.Column([
	[sg.Text("Disp Per90")],
	[sg.In(key='-fps5-',size = (10, 1))],
	[sg.In(key='-fpt5-',size = (10, 1))],
	[sg.Text("",key="-result51-")],
	[sg.Text("LongB Per90",size = (10, 1))],
	[sg.In(key='-mps5-',size = (10, 1))],
	[sg.In(key='-mpt5-',size = (10, 1))],
	[sg.Text("",key="-result52-")],
	[sg.Text("AerialDW Per90")],
	[sg.In(key='-dps5-',size = (10, 1))],
	[sg.In(key='-dpt5-',size = (10, 1))],
	[sg.Text("",key="-result53-")]])

column6 = sg.Column([
	[sg.Text(" Per90")],
	[sg.In(key='-fps6-',size = (10, 1))],
	[sg.In(key='-fpt6-',size = (10, 1))],
	[sg.Text("",key="-result61-")],
	[sg.Text(" Per90",size = (10, 1))],
	[sg.In(key='-mps6-',size = (10, 1))],
	[sg.In(key='-mpt6-',size = (10, 1))],
	[sg.Text("",key="-result62-")],
	[sg.Text(" Per90")],
	[sg.In(key='-dps6-',size = (10, 1))],
	[sg.In(key='-dpt6-',size = (10, 1))],
	[sg.Text("",key="-result63-")]])
	
layout = [[labelsColumn,column1,column2,column3,column4,column5,column6],
		[sg.Button("Push Button",key="-PushButton-",size = (20, 1)),sg.Button("Exit",key="-Exit-",size = (20, 1))],
		[sg.Text("This area can be used to expain for your application.")]]

# Create the window
window = sg.Window("Football Player Stat Analysis", layout)

# Create an event loop
while True:
	event, values = window.read()
	
	#checking for press Exit button
	if event == "-PushButton-" :
		value = float(values["-dps6-"])
		result = fbs.sth_d(value)
		window["-dpt6-"].update(result)
	if event == "-PushButton-" :
		value = float(values["-dps5-"])
		result = fbs.aerial_d(value)
		window["-dpt5-"].update(result)
	if event == "-PushButton-" :
		value = float(values["-dps4-"])
		result = fbs.longb_d(value)
		window["-dpt4-"].update(result)
	if event == "-PushButton-" :
		value = float(values["-dps3-"])
		result = fbs.dribbledp_d(value)
		window["-dpt3-"].update(result)
	if event == "-PushButton-" :
		value = float(values["-dps2-"])
		result = fbs.inter_d(value)
		window["-dpt2-"].update(result)
	if event == "-PushButton-" :
		value = float(values["-dps1-"])
		result = fbs.tackles_d(value)
		window["-dpt1-"].update(result)
	if event == "-PushButton-":
		list1 = values["-dpt6-"], values["-dpt5-"], values["-dpt4-"], values["-dpt3-"], values["-dpt2-"], values["-dpt1-"]
		result = fbs.overall(list1)
		#[str(values["-dpt1-"]), str(values["-dpt2-"]), str(values["-dpt3-"]), str(values["-dpt4-"]), str(values["-dpt5-"])]
		window["-result53-"].update(result)
	
	#checking for press Exit button or close window
	if event == "-Exit-" or event == sg.WIN_CLOSED:
		break

window.close()