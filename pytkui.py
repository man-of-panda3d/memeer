import json
import tkinter
import tkinter.filedialog
from tkinter import ttk
from tksheet import Sheet
import pyback
import p3dfunc
import tkinter.scrolledtext as scrolledtext
from tkinter import BOTH, END, LEFT
import pprint
from tkinter import messagebox 
from pathlib import Path
import yaml
from PIL import ImageTk, Image
import time

def addstdframe (root, framedesc, width=900, height=600):
	nframe = tkinter.Frame(root, width=width, height=600)
	root.add(nframe, text=framedesc)
	return nframe

def addcnvframe (root, framedesc):
	def myfunction(event):
		mcanvas.configure(scrollregion=mcanvas.bbox("all"), width=900, height=600)
	def on_mousewheel(event):
		if (event.num == 5 or event.delta < -100): count = 1 
		if (event.num == 4 or event.delta > 100) : count = -1 
		try: count
		except NameError: count = None
		if count is None: print(event)
		mcanvas.yview_scroll(count, "units")
	mframe = addstdframe(root, framedesc, width=900, height=600)
	mcanvas=tkinter.Canvas(mframe, width=900, height=600)
	nframe = tkinter.Frame(mcanvas, width=900, height=600)
	myscrollbar=tkinter.Scrollbar(mframe, orient="vertical", command=mcanvas.yview)
	mcanvas.configure(yscrollcommand=myscrollbar.set)
	myscrollbar.pack(side="right", fill="y")
	mcanvas.pack (side="left")
	mcanvas.create_window ((0,0), window=nframe, anchor='nw')
	nframe.bind("<Configure>",myfunction)
	nframe.bind('<MouseWheel>', on_mousewheel)
	return nframe

def on_canvas_mousewheel(event, lvl=2):
	grandparent = event.widget.master.master if lvl==2 else event.widget.master.master.master
	if (event.num == 5 or event.delta < -100): count = 1 
	if (event.num == 4 or event.delta > 100) : count = -1 
	try: count
	except NameError: count = None
	if count is None: print(event)
	grandparent.yview_scroll(count, "units")

def scrllabel (framep = {}, text = '<MISSING>', column=1, row=1, columnspan=1, sticky='nw', scroll = 1):
	newlbl = ttk.Label(framep, text=text)
	newlbl.grid(column=column, row=row, columnspan=columnspan, sticky=sticky)
	if scroll == 1: newlbl.bind('<MouseWheel>', lambda eff: on_canvas_mousewheel (eff, lvl=2))
	return newlbl

def newentry (framep='', width=0, col=0, row=0, colspan=1, text='', lbltext = '', sticky='nw', retlbl = 0):
	if lbltext != '': label = scrllabel (framep = framep, text = lbltext, column=col-1, row=row, sticky='ne')
	entry_text= ttk.Entry(framep, width=width)
	entry_text.grid(column=col, row=row, sticky=sticky, columnspan=colspan)
	entry_text.bind('<MouseWheel>', lambda eff: on_canvas_mousewheel (eff, lvl=2))
	entry_text.insert(0, text)
	if retlbl != 0: return {"label": label, "entry": entry_text}
	return entry_text
	

def newscrolltext (framep = {}, text = '', column=0, row=0, width=10, height=5, columnspan = 0, rowspan = 0):
	scrolltext = scrolledtext.ScrolledText(framep, undo=True, width=60, height=5)
	scrolltext.grid(column=1, row=row, columnspan=columnspan, rowspan = rowspan)
	scrolltext.bind('<MouseWheel>', lambda eff: on_canvas_mousewheel (eff, lvl=3))
	scrolltext.insert(1.0, text)
	return scrolltext

def modifyentry (entry_elem = {}, text = '<MISSING>', start = 0):
	entry_elem.delete(start, END)
	entry_elem.insert(start, text)

def refresh_universe(uielem = {}, conf_frames = {}, appsetup = {}):
	for code, frames in conf_frames.items():
		if code == 'conf': continue
		for tkitemls in frames.winfo_children():
			tkitemls.destroy()
	univ = pyback.getUniverseData (user = uielem['conf']['auser'].get(), folder = uielem['conf']['folder'].get(), appset = appsetup)
	modifyentry(entry_elem = uielem['conf']['detail'], text = appsetup['project']['detail'])
	modifyentry(entry_elem = uielem['conf']['winsize'], text = appsetup['project']['winsize'])
	modifyentry(entry_elem = uielem['conf']['fps'], text = appsetup['project']['fps'])
	uielem['conf']['preview'].state(['selected'])
	appuisetup (appset = appsetup, root = conf_frames['conf'], uiset = uielem['conf'])
	actsuisetup (root = conf_frames['acts'], uiset = uielem['acts'], actions = univ['actions'])
	objsuisetup (root = conf_frames['objs'], uiset = uielem['objs'], objects = univ['objects'])
	logixuisetup (root = conf_frames['logix'], uiset = uielem['logix'], logix = univ['logicals'])
	return univ

def newchkbox (root = {}, text = '<MISSING>', value = 0, column=0, row=0):
	chkbox_ui = ttk.Checkbutton(root, text=text)
	chkbox_ui.state(['!alternate'])
	chkbox_ui.state(['selected']) if value == 1 else chkbox_ui.state(['!alternate'])
	chkbox_ui.grid(column=column, row=row)
	return chkbox_ui

def appuisetup (appset = {}, root = {}, uiset = {}, retry=1):
	ttk.Label(root, text="\t\t\t").grid(column=2, row=1)
	uiset['auser'] = newentry (framep=root, width=90, col=3, row=2, text=appset['user_idnt'], lbltext = 'User Identity')
	uiset['apkey'] = newentry (framep=root, width=90, col=3, row=3, text=appset['secrettxt'], lbltext = 'Secret Passkey')
	uiset['folder'] = newentry (framep=root, width=90, col=3, row=4, text=appset['project']['folder'], lbltext = 'Project Folder')
	uiset['detail'] = newentry (framep=root, width=90, col=3, row=5, text=appset['project']['detail'], lbltext = 'Project Description')
	uiset['winsize'] = newentry (framep=root, width=10, col=3, row=6, text=appset['project']['winsize'], lbltext = 'Screen resolution')
	uiset['fps'] = newentry (framep=root, width=2, col=3, row=7, text=appset['project']['fps'], lbltext = 'Frame Rate')
	uiset['preview'] = newchkbox (root = root, text = 'In Preview mode (not production ready)', value = appset['project']['preview'], column=3, row=11)
	uiset['expand'] = newchkbox (root = root, text = 'Expansion for Verb Synonyms', value = appset['project']['expand'], column=2, row=11)

def port_conf_save (uielems, appsetup, univ):
	appsetup['user_idnt'] = uielems['auser'].get()
	appsetup['secrettxt'] = uielems['apkey'].get()
	appsetup['project']['folder'] = uielems['folder'].get()
	appsetup['project']['detail'] = uielems['detail'].get()
	appsetup['project']['winsize'] = uielems['winsize'].get()
	appsetup['project']['fps'] = uielems['fps'].get()
	appsetup['project']['preview'] = 1 if uielems['preview'].instate(['selected']) else 0
	appsetup['project']['expand'] = 1 if uielems['expand'].instate(['selected']) else 0
	pyback.port_conf_save(appsetup)

def storyroomsetup (lstory, projvars = {}, boarditems = {}, session = {}):
	csize = 500
	def savePosn(event):
		global lastx, lasty
		lastx, lasty = event.x, event.y
		coordbox.delete('1.0', END)
		coordbox.insert(1.0, pprint.pformat(session['coords'], indent=2))
		session['coords'].append([lastx, lasty])
	def deletePosn(event):
		canvas.delete("all")
		coordbox.delete('1.0', END)
		session['coords'] = []
	def addLine(event):
		canvas_id = canvas.create_line((lastx, lasty, event.x, event.y))
		savePosn(event)
	def loadCombobox (root = {}, lovalues = (), col=0, row=0, colspan = 1):
		countryvar = tkinter.StringVar()
		country = ttk.Combobox(root, textvariable=countryvar)
		country.grid(column=col, row=row, sticky='n', columnspan=colspan)
		country['values'] = lovalues
		country.state(["readonly"])
		return country
	storybox = scrolledtext.ScrolledText(lstory, undo=True, width=51, height=31)
	storybox.grid(column=0, row=0, sticky='n')
	coordbox = scrolledtext.ScrolledText(lstory, undo=True, width=51, height=6)
	coordbox.grid(column=0, row=1, sticky='n', rowspan=3)
	canvas = tkinter.Canvas(lstory, width=500, height=500, background='gray75')
	canvas.grid(column=1, row=0, columnspan=5)
	canvas.bind("<Button-1>", savePosn)
	canvas.bind("<Button-3>", deletePosn)
	canvas.bind("<B1-Motion>", addLine)
	def updatelvl (event):
		sel = list(listboxl1.curselection())[0]
		lvl1key = listboxl1.get(sel)
		listboxl2.delete(0, END)
		for ix, lb11vals in enumerate(list(boarditems[sel].values())[0]):
			listboxl2.insert(ix, list(lb11vals.keys())[0])
	listboxl1 = tkinter.Listbox(lstory, height = 5, width = 15, activestyle = 'dotbox', exportselection=0)
	listboxl1.grid(column=1, row=1, sticky='nw', rowspan=2)
	listboxl1.bind("<<ListboxSelect>>", updatelvl)
	for ix, lb11vals in enumerate(boarditems): listboxl1.insert(ix, list(lb11vals.keys())[0])
	def loadparams (event):
		sel1 = list(listboxl1.curselection())[0]
		sel2 = list(listboxl2.curselection())[0]
		params = list(list(boarditems[sel1].values())[0][sel2].values())[0]
		for ix in range(0, 3):
			param_ent[ix]['label'].grid_remove()
			param_ent[ix]['entry'].grid_remove()
			modifyentry(entry_elem = param_ent[ix]['entry'], text = "")
		for ix in range(0, 3):
			if len(params) <= ix: continue
			param_ent[ix]['label'].grid()
			param_ent[ix]['entry'].grid()
			modifyentry(entry_elem = param_ent[ix]['entry'], text = pyback.entdefaultparams (ix, params, projvars))
			param_ent[ix]['label'].config(text = params[ix])
		return 1
	listboxl2 = tkinter.Listbox(lstory, height = 5, width = 20, activestyle = 'dotbox', exportselection=0)
	listboxl2.grid(column=2, row=1, sticky='nw', rowspan=2)
	listboxl2.bind("<<ListboxSelect>>", loadparams)
	param_ent = []
	for ix in range(0, 3):
		paramix = newentry (framep=lstory, width=10, col=5, row=ix+1, text='', lbltext='Not needed', retlbl = 1)
		param_ent.append(paramix)
	lstoryui = {'storybox': storybox, 'canvas': canvas, 'coordbox': coordbox, 'lbox1': listboxl1, 'lbox2': listboxl2, 'param_ent': param_ent}
	return lstoryui

def actsuiread (uiset = [], expand = 1):
	retval = []
	synofile = Path("verbforms.js")
	with open(synofile) as lujs: verbjs = json.load(lujs)
	for acta in uiset:
		lact = {'func': acta['func']}
		verbsyns = pyback.splittext (text = acta['syns'].get())
		lact['syns'] = pyback.loadsynos(verbsyns, verbjs, expand)
		modifyentry(entry_elem = acta['syns'], text = ", ".join(lact['syns']))
		lact['jjrb'] = pyback.splittext (text = acta['jjrb'].get())
		retval.append(lact)
	return retval

def actsuisetup (root = {}, uiset = [], actions = []):
	ttk.Label(root, text='Functions: "move", "locate", "vanish" are common for all').grid(column=0, row=0, columnspan=3, sticky='nw')
	ttk.Label(root, text='Suffix "+" for default expasion, "-" to never expand').grid(column=0, row=1, columnspan=3, sticky='nw')
	rownum = 2
	for actid, action in enumerate(actions):
		scrllabel (framep = root, text = '-'*100, column=0, row=rownum, columnspan=2, sticky='nw')
		lactui = {'actid': actid}
		if 'func' not in action: continue
		lactui['func'] = action['func']
		scrllabel (framep = root, text = "Function Name: "+action['func'], column=0, row=rownum, sticky='nw')
		lactui['syns'] = newentry (framep=root, width=40, col=1, row=rownum+1, colspan=1, text=', '.join(action['syns']), lbltext='Synonyms')
		lactui['jjrb'] = newentry (framep=root, width=40, col=2, row=rownum+1, colspan=1, text=', '.join(action['jjrb']), lbltext='Modifiers')
		rownum = rownum + 2
		uiset.append(lactui)

def objsuiread (uiset = []):
	retval = []
	for obj in uiset:
		lobj = {'file': obj['file'], 'acts': {}}
		lobj['syns'] = pyback.splittext (text = obj['syns'].get())
		lobj['jjrb'] = pyback.splittext (text = obj['jjrb'].get())
		lobj['move'] = pyback.splittext (text = obj['move'].get())
		for macts in obj['acts']:
			mfdet = {'fstart': int(macts['fstart'].get()), 'flast': int(macts['flast'].get())}
			lobj['acts'][macts['afile']] = mfdet
		lobj['joint'] = obj['joint'].get()
		retval.append(lobj)
	return retval

def objsuisetup (root = {}, uiset = [], objects = []):
	rownum = 0
	for modid, model in enumerate(objects):
		scrllabel (framep = root, text = '-'*120, column=0, row=rownum, columnspan=3, sticky='nw')
		objdets = model['file'] + " (animations: " + ', '.join(list(model['acts'].keys())) + ")"
		lobjui = {'file': model['file'], 'modid': modid, 'acts': []}
		scrllabel (framep = root, text = 'Model list: '+objdets, column=0, row=rownum, columnspan=3, sticky='nw')
		lobjui['syns'] = newentry (framep=root, width=40, col=1, row=rownum+1, colspan=1, text=', '.join(model['syns']), lbltext='Synonyms')
		lobjui['jjrb'] = newentry (framep=root, width=40, col=3, row=rownum+1, colspan=1, text=', '.join(model['jjrb']), lbltext='Modifiers')
		lobjui['move'] = newentry (framep=root, width=40, col=1, row=rownum+2, colspan=1, text=', '.join(model['move']), lbltext='Movement')
		lobjui['joint'] = newentry (framep=root, width=40, col=3, row=rownum+2, colspan=1, text=model['joint'], lbltext='Joint Group')
		rownum = rownum + 3
		for afile, actdet in model['acts'].items():
			lobjfui = {'afile': afile}
			scrllabel (framep = root, text = 'Model '+model['file']+', Action file: '+afile, column=0, row=rownum, sticky='ne')
			lobjfui['fstart'] = newentry (framep=root, width=10, col=3, row=rownum, text=actdet['fstart'], lbltext='Play between frames', sticky='nw')
			lobjfui['flast'] = newentry (framep=root, width=10, col=3, row=rownum, text=actdet['flast'], sticky='ne')
			lobjui['acts'].append(lobjfui)
			rownum = rownum + 1
		uiset.append(lobjui)

def logixuiread (llogixui):
	retval = []
	for llist in llogixui:
		logic = {}
		if llist['basic'].get() == '': continue
		logic['basic'] = p3dfunc.storyparse(llist['basic'].get())[0]
		if logic['basic'] == '': continue
		logic['addon'] = p3dfunc.storyparse(llist['addon'].get('1.0', tkinter.END))
		retval.append(logic)
	return retval

def logixuisetup (root = {}, uiset = [], logix = []):
	rownum = 0
	for logid, 	logic in enumerate(logix+[{'basic': '', 'addon': []}]):
		ttk.Label(root, text='-'*100).grid(column=0, row=rownum, columnspan=2, sticky='nw')
		llogcui = {'logid': logid}
		llogcui['basic'] = newentry (framep=root, width=120, col=1, row=rownum+1, colspan=8, text=logic['basic'], lbltext='Current condition')
		ttk.Label(root, text='Extra steps').grid(column=0, row=rownum+2, sticky='nw')
		indexbox = scrolledtext.ScrolledText(root, undo=True, width=90, height=5)
		indexbox.grid(column=1, row=rownum+2, columnspan=5)
		indexbox.insert(1.0, "\n".join(logic['addon']))
		indexbox.bind('<MouseWheel>', on_canvas_mousewheel)
		llogcui['addon'] = indexbox
		rownum=rownum+3
		uiset.append(llogcui)

def exec_play_frame (entparams = [], appsetup = {}, uielem = {}, root = {}):
	fromfr = 1 if pyback.forceint(entparams[0]) == -1 else pyback.forceint(entparams[0])
	tillfr = 9999 if pyback.forceint(entparams[1]) == -1 else pyback.forceint(entparams[1])
	fps = appsetup['project']['fps'] if pyback.forceint(entparams[2]) == -1 else pyback.forceint(entparams[2])
	imgdest = appsetup['project']['folder']+'/rushes/'
	print ("fromfr, tillfr, fps", fromfr, tillfr, fps)
	for frid in range(fromfr, tillfr+1):
		imgfile = imgdest+"rush__"+"%04d"%(frid)+".png"
		print ("imgfile", imgfile)
		image = Image.open(imgfile)
		image = image.resize((500, 500), Image.ANTIALIAS)
		root.myimg = myimg = ImageTk.PhotoImage(image)
		uielem['canvas'].create_image((0,0), image=myimg, anchor='nw')
		uielem['canvas'].update()
		time.sleep(1/fps)
	return {'imgdest': imgdest, 'frame': tillfr+1}
