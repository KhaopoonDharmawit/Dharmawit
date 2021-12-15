import PySimpleGUI as sg
import fb_stat as fbs

font = ("Arial", 6)
font2 = ("Arial", 7)

labelsColumn = sg.Column([
	[sg.Text("Forwards")],
	[sg.Text("Player Stats")],
	[sg.Text("Player Tier")],
	[sg.Text("")],
	[sg.Text("")],
	[sg.Text("Midfielders")],
	[sg.Text("Player Stats")],
	[sg.Text("Player Tier")],
	[sg.Text("")],
	[sg.Text("")],
	[sg.Text("Defenders")],
	[sg.Text("Player Stats")],
	[sg.Text("Player Tier")],
	[sg.Text("")],
	[sg.Text("")]])

column1 = sg.Column([
	[sg.Text("xG Per90")],
	[sg.In(key='-fps1-',size = (10, 1))],
	[sg.In(key='-fpt1-',size = (10, 1))],
	[sg.Text("",key="-result11-")],
	[sg.Text("")],
	[sg.Text("KeyP Per90",size = (10, 1))],
	[sg.In(key='-mps1-',size = (10, 1))],
	[sg.In(key='-mpt1-',size = (10, 1))],
	[sg.Text("",key="-result12-")],
	[sg.Text("")],
	[sg.Text("Tackles Per90")],
	[sg.In(key='-dps1-',size = (10, 1))],
	[sg.In(key='-dpt1-',size = (10, 1))],
	[sg.Text("",key="-result13-")],
	[sg.Text("")]])

column2 = sg.Column([
	[sg.Text("Shots Per90")],
	[sg.In(key='-fps2-',size = (10, 1))],
	[sg.In(key='-fpt2-',size = (10, 1))],
	[sg.Text("",key="-result21-")],
	[sg.Text("")],
	[sg.Text("PassSuc %",size = (10, 1))],
	[sg.In(key='-mps2-',size = (10, 1))],
	[sg.In(key='-mpt2-',size = (10, 1))],
	[sg.Text("",key="-result22-")],
	[sg.Text("")],
	[sg.Text("Inter Per90")],
	[sg.In(key='-dps2-',size = (10, 1))],
	[sg.In(key='-dpt2-',size = (10, 1))],
	[sg.Text("",key="-result23-")],
	[sg.Text("")]])
	
column3 = sg.Column([
	[sg.Text("KeyP Per90")],
	[sg.In(key='-fps3-',size = (10, 1))],
	[sg.In(key='-fpt3-',size = (10, 1))],
	[sg.Text("",key="-result31-")],
	[sg.Text("")],
	[sg.Text("Dribbles Per90" )],
	[sg.In(key='-mps3-',size = (10, 1))],
	[sg.In(key='-mpt3-',size = (10, 1))],
	[sg.Text("",key="-result32-")],
	[sg.Text("")],
	[sg.Text("DribbledP Per90")],
	[sg.In(key='-dps3-',size = (10, 1))],
	[sg.In(key='-dpt3-',size = (10, 1))],
	[sg.Text("",key="-result33-")],
	[sg.Text("")]])
	
column4 = sg.Column([
	[sg.Text("Dribbles Per90")],
	[sg.In(key='-fps4-',size = (10, 1))],
	[sg.In(key='-fpt4-',size = (10, 1))],
	[sg.Text("",key="-result41-")],
	[sg.Text("")],
	[sg.Text("Disp Per90",size = (10, 1))],
	[sg.In(key='-mps4-',size = (10, 1))],
	[sg.In(key='-mpt4-',size = (10, 1))],
	[sg.Text("",key="-result42-")],
	[sg.Text("")],
	[sg.Text("LongB Per90")],
	[sg.In(key='-dps4-',size = (10, 1))],
	[sg.In(key='-dpt4-',size = (10, 1))],
	[sg.Text("",key="-result43-")],
	[sg.Text("")]])

column5 = sg.Column([
	[sg.Text("Disp Per90")],
	[sg.In(key='-fps5-',size = (10, 1))],
	[sg.In(key='-fpt5-',size = (10, 1))],
	[sg.Text("",key="-result51-")],
	[sg.Text("")],
	[sg.Text("LongB Per90",size = (10, 1))],
	[sg.In(key='-mps5-',size = (10, 1))],
	[sg.In(key='-mpt5-',size = (10, 1))],
	[sg.Text("",key="-result52-")],
	[sg.Text("")],
	[sg.Text("AerialDW Per90")],
	[sg.In(key='-dps5-',size = (10, 1))],
	[sg.In(key='-dpt5-',size = (10, 1))],
	[sg.Text("",key="-result53-")],
	[sg.Text("")]])

column6 = sg.Column([
	[sg.Text("AerialDW Per90")],
	[sg.In(key='-fps6-',size = (10, 1))],
	[sg.In(key='-fpt6-',size = (10, 1))],
	[sg.Text("",key="-result61-")],
	[sg.Text("")],
	[sg.Text("Tackles Per90",size = (10, 1))],
	[sg.In(key='-mps6-',size = (10, 1))],
	[sg.In(key='-mpt6-',size = (10, 1))],
	[sg.Text("",key="-result62-")],
	[sg.Text("")],
	[sg.Text("Blocks Per90")],
	[sg.In(key='-dps6-',size = (10, 1))],
	[sg.In(key='-dpt6-',size = (10, 1))],
	[sg.Text("",key="-result63-")],
	[sg.Text("")]])

column7 = sg.Column([
	[sg.Text("")],
	[sg.In(key='-foverall-',size = (20, 2))],
	[sg.Text("")],
	[sg.Text("")],
	[sg.In(key='-moverall-',size = (20, 2))],
	[sg.Text("")],
	[sg.Text("")],
	[sg.In(key='-doverall-',size = (20, 2))],
	[sg.Text("")]])
	
layout = [[labelsColumn,column1,column2,column3,column4,column5,column6],
		[sg.Text("xG Per90: Expected Goal per 90 mins   Shots Per90: Total Shots per 90 mins   KeyP Per90: Key Passes per 90 mins   Dribbles Per90: Dribbles per 90 mins   Disp Per90: Dispossessed per 90 mins   PassSuc %: Pass Success Percentage", font=font)],
		[sg.Text("LongB Per90: Long Balls per 90 mins   Tackles Per90: Tackles per 90 mins   Inter Per90: Interceptions per 90 mins   DribbledP Per90: Dribbled Past per 90 mins   AerialDW Per90: Aerial Duels won per 90 mins   Blocks Per90: Blocks per 90 mins", font=font)],
		[sg.Text("")],
		[sg.Button("Evaluate For",key="-Evaluate For-",size = (20, 1)),sg.Button("Evaluate Mid",key="-Evaluate Mid-",size = (20, 1)),sg.Button("Evaluate Def",key="-Evaluate Def-",size = (20, 1))],
		[sg.Button("Clear",key="-Clear-",size = (10, 1))]]#,sg.Button("Exit",key="-Exit-",size = (10 , 1))
		


# Create the window
window = sg.Window("Football Player Stat Analysis", layout, size=(875,550))

# Create an event loop
while True:
	event, values = window.read()
	
	#checking for press Exit button
	if event == "-Evaluate Def-" :
		value1 = float(values["-dps6-"])
		result1 = fbs.blocks_d(value1)
		window["-dpt6-"].update(result1)
		
		value2 = float(values["-dps5-"])
		result2 = fbs.aerial_d(value2)
		window["-dpt5-"].update(result2)
		
		value3 = float(values["-dps4-"])
		result3 = fbs.longb_d(value3)
		window["-dpt4-"].update(result3)
		
		value4 = float(values["-dps3-"])
		result4 = fbs.dribbledp_d(value4)
		window["-dpt3-"].update(result4)
		
		value5 = float(values["-dps2-"])
		result5 = fbs.inter_d(value5)
		window["-dpt2-"].update(result5)
		
		value6 = float(values["-dps1-"])
		result6 = fbs.tackles_d(value6)
		window["-dpt1-"].update(result6)
		
		#list1 = values["-dpt6-"], values["-dpt5-"], values["-dpt4-"], values["-dpt3-"], values["-dpt2-"], values["-dpt1-"]
		list1 = result1, result2, result3, result4, result5, result6
		result = fbs.overall(list1)
		window["-result63-"].update(result, font=font2)
	
	elif event == "-Evaluate Mid-":
		value1 = float(values["-mps6-"])
		result1 = fbs.tackles_m(value1)
		window["-mpt6-"].update(result1)
		
		value2 = float(values["-mps5-"])
		result2 = fbs.longb_m(value2)
		window["-mpt5-"].update(result2)
		
		value3 = float(values["-mps4-"])
		result3 = fbs.disp_m(value3)
		window["-mpt4-"].update(result3)
		
		value4 = float(values["-mps3-"])
		result4 = fbs.dribbles_m(value4)
		window["-mpt3-"].update(result4)
		
		value5 = float(values["-mps2-"])
		result5 = fbs.passsuc_m(value5)
		window["-mpt2-"].update(result5)
		
		value6 = float(values["-mps1-"])
		result6 = fbs.keyp_m(value6)
		window["-mpt1-"].update(result6)
		
		list1 = result1, result2, result3, result4, result5, result6
		result = fbs.overall(list1)
		window["-result62-"].update(result, font=font2)

	elif event == "-Evaluate For-":
		value1 = float(values["-fps6-"])
		result1 = fbs.aerial_f(value1)
		window["-fpt6-"].update(result1)
		
		value2 = float(values["-fps5-"])
		result2 = fbs.disp_f(value2)
		window["-fpt5-"].update(result2)
		
		value3 = float(values["-fps4-"])
		result3 = fbs.dribbles_f(value3)
		window["-fpt4-"].update(result3)
		
		value4 = float(values["-fps3-"])
		result4 = fbs.keyp_f(value4)
		window["-fpt3-"].update(result4)
		
		value5 = float(values["-fps2-"])
		result5 = fbs.shots_f(value5)
		window["-fpt2-"].update(result5)
		
		value6 = float(values["-fps1-"])
		result6 = fbs.xG_f(value6)
		window["-fpt1-"].update(result6)
		
		list1 = result1, result2, result3, result4, result5, result6
		result = fbs.overall(list1)
		window["-result61-"].update(result, font=font2)


	elif event == "-Clear-":
		window["-dpt6-"].update("")
		window["-dpt5-"].update("")
		window["-dpt4-"].update("")
		window["-dpt3-"].update("")
		window["-dpt2-"].update("")
		window["-dpt1-"].update("")
		window["-dps6-"].update("")
		window["-dps5-"].update("")
		window["-dps4-"].update("")
		window["-dps3-"].update("")
		window["-dps2-"].update("")
		window["-dps1-"].update("")
		window["-mpt6-"].update("")
		window["-mpt5-"].update("")
		window["-mpt4-"].update("")
		window["-mpt3-"].update("")
		window["-mpt2-"].update("")
		window["-mpt1-"].update("")
		window["-mps6-"].update("")
		window["-mps5-"].update("")
		window["-mps4-"].update("")
		window["-mps3-"].update("")
		window["-mps2-"].update("")
		window["-mps1-"].update("")
		window["-fpt6-"].update("")
		window["-fpt5-"].update("")
		window["-fpt4-"].update("")
		window["-fpt3-"].update("")
		window["-fpt2-"].update("")
		window["-fpt1-"].update("")
		window["-fps6-"].update("")
		window["-fps5-"].update("")
		window["-fps4-"].update("")
		window["-fps3-"].update("")
		window["-fps2-"].update("")
		window["-fps1-"].update("")
		window["-result61-"].update("")
		window["-result62-"].update("")
		window["-result63-"].update("")

	#checking for press Exit button or close window
	elif event == sg.WIN_CLOSED: #event == "-Exit-" or 
		break

window.close()