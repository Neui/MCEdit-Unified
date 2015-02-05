#.# Marks the layout modifications. -- D.C.-G.
from config import config
import albow
import mceutils
from pygame import key
from albow.dialogs import Dialog
from albow.translate import _
from glbackground import Panel
from albow import Button, Column

ESCAPE = '\033'


def remapMouseButton(button):
    buttons = [0, 1, 3, 2, 4, 5, 6, 7]  # mouse2 is right button, mouse3 is middle
    if button < len(buttons):
        return buttons[button]
    return button


class KeyConfigPanel(Dialog):
    keyConfigKeys = [
        "<Movement>",
        "Forward",
        "Back",
        "Left",
        "Right",
        "Up",
        "Down",
        "Brake",
        "",
        "<Camera>",
        "Pan Up",
        "Pan Down",
        "Pan Left",
        "Pan Right",
        "Toggle View",
        "Goto Panel",
        "View Distance",
        "Toggle Renderer",
        "Fly Mode",
        "",
        "<Selection>",
        "Increase Reach",
        "Decrease Reach",
        "Reset Reach",
        "Show Block Info",
        "Pick Block",
        "Snap Clone to Axis",
        "Long-Distance Mode",
        "Blocks-Only Modifier",
        "",
        "<Brush Tool>",
        "Rotate (Brush)",
        "Roll (Brush)",
        "Increase Brush",
        "Decrease Brush",
        "Brush Line Tool",
        "",
        "<Clone Tool>",
        "Rotate (Clone)",
        "Roll (Clone)",
        "Flip",
        "Mirror",
        "",
        "<Fill and Replace Tool>",
        "Replace Shortcut",
        "Swap",
        "",
        "<Chunk Control Tool>",
        "Select Chunks",
        "Deselect Chunks",
        "",
        "<Function>",
        "Delete Blocks",
        "Select All",
        "Deselect",
        "Undo",
        "Redo",
        "Cut",
        "Copy",
        "Paste",
        "Export Selection",
        "",
        "<Menu>",
        "New World",
        "Quick Load",
        "Open",
        "Save",
        "Reload World",
        "Close World",
        "World Info",
        "Quit",
        "",
        "<Miscellaneous>",
        "Take a Screenshot",
        "Debug Overlay",
        "Fast Nudge",
        "Fast Increment Modifier"
    ]

    otherNames = {
        "Goto Panel": "Goto Position",
        "Show Block Info": "Show Block Info (Hold)",
        "Pick Block": "Pick Block (Hold + Click)",
        "Snap Clone to Axis": "Snap Clone to Axis (Hold)",
        "Blocks-Only Modifier": "Blocks-Only Modifier (Hold)",
        "Rotate (Brush)": "Rotate",
        "Roll (Brush)": "Roll",
        "Increase Brush": "Increase Size",
        "Decrease Brush": "Decrease Size",
        "Brush Line Tool": "Line Tool (Hold)",
        "Rotate (Clone)": "Rotate",
        "Roll (Clone)": "Roll",
        "Replace Shortcut": "Replace",
        "Select Chunks": "Select Chunks (Hold)",
        "Deselect Chunks": "Deselect Chunks (Hold)",
        "Delete Blocks": "Delete",
        "Export Selection": "Export",
        "Take a Screenshot": "Take Screenshot"
    }

    presets = {
                "WASD": [
                    ("Forward", "W"),
                    ("Back", "S"),
                    ("Left", "A"),
                    ("Right", "D"),
                    ("Up", "Space"),
                    ("Down", "Shift"),
                    ("Brake", "C"),

                    ("Pan Up", "I"),
                    ("Pan Down", "K"),
                    ("Pan Left", "J"),
                    ("Pan Right", "L"),
                    ("Toggle View", "Tab"),
                    ("Goto Panel", "Ctrl-G"),
                    ("View Distance", "Ctrl-F"),
                    ("Toggle Renderer", "Ctrl-M"),
                    ("Fly Mode", "None"),

                    ("Increase Reach", "Scroll Up"),
                    ("Decrease Reach", "Scroll Down"),
                    ("Reset Reach", "Button 3"),
                    ("Show Block Info", "Alt"),
                    ("Pick Block", "Alt"),
                    ("Snap Clone to Axis", "Ctrl"),
                    ("Long-Distance Mode", "Alt-Z"),
                    ("Blocks-Only Modifier", "Alt"),

                    ("Rotate (Brush)", "E"),
                    ("Roll (Brush)", "G"),
                    ("Increase Brush", "R"),
                    ("Decrease Brush", "F"),
                    ("Brush Line Tool", "Z"),

                    ("Rotate (Clone)", "E"),
                    ("Roll (Clone)", "R"),
                    ("Flip", "F"),
                    ("Mirror", "G"),

                    ("Replace Shortcut", "R"),
                    ("Swap", "X"),

                    ("Select Chunks", "Z"),
                    ("Deselect Chunks", "Alt"),

                    ("Delete Blocks", "Delete"),
                    ("Select All", "Ctrl-A"),
                    ("Deselect", "Ctrl-D"),
                    ("Undo", "Ctrl-Z"),
                    ("Redo", "Ctrl-Y"),
                    ("Cut", "Ctrl-X"),
                    ("Copy", "Ctrl-C"),
                    ("Paste", "Ctrl-V"),
                    ("Export Selection", "Ctrl-E"),

                    ("New World", "Ctrl-N"),
                    ("Quick Load", "Ctrl-L"),
                    ("Open", "Ctrl-O"),
                    ("Save", "Ctrl-S"),
                    ("Reload World", "Ctrl-R"),
                    ("Close World", "Ctrl-W"),
                    ("World Info", "Ctrl-I"),
                    ("Quit", "Ctrl-Q"),

                    ("Take a Screenshot", "F6"),
                    ("Debug Overlay", "0"),
                    ("Fast Nudge", "None"),
                    ("Fast Increment Modifier", "Ctrl")
                ],
                "Arrows": [
                    ("Forward", "Up"),
                    ("Back", "Down"),
                    ("Left", "Left"),
                    ("Right", "Right"),
                    ("Up", "Page Up"),
                    ("Down", "Page Down"),
                    ("Brake", "Space"),

                    ("Pan Up", "I"),
                    ("Pan Down", "K"),
                    ("Pan Left", "J"),
                    ("Pan Right", "L"),
                    ("Toggle View", "Tab"),
                    ("Goto Panel", "Ctrl-G"),
                    ("View Distance", "Ctrl-F"),
                    ("Toggle Renderer", "Ctrl-M"),
                    ("Fly Mode", "None"),

                    ("Increase Reach", "Scroll Up"),
                    ("Decrease Reach", "Scroll Down"),
                    ("Reset Reach", "Button 3"),
                    ("Show Block Info", "Alt"),
                    ("Pick Block", "Alt"),
                    ("Snap Clone to Axis", "Ctrl"),
                    ("Long-Distance Mode", "Alt-Z"),
                    ("Blocks-Only Modifier", "Alt"),

                    ("Rotate (Brush)", "Home"),
                    ("Roll (Brush)", "Delete"),
                    ("Increase Brush", "End"),
                    ("Decrease Brush", "Insert"),
                    ("Brush Line Tool", "Z"),

                    ("Rotate (Clone)", "Home"),
                    ("Roll (Clone)", "End"),
                    ("Flip", "Insert"),
                    ("Mirror", "Delete"),

                    ("Replace Shortcut", "R"),
                    ("Swap", "\\"),

                    ("Select Chunks", "Z"),
                    ("Deselect Chunks", "Alt"),

                    ("Delete Blocks", "Backspace"),
                    ("Select All", "Ctrl-A"),
                    ("Deselect", "Ctrl-D"),
                    ("Undo", "Ctrl-Z"),
                    ("Redo", "Ctrl-Y"),
                    ("Cut", "Ctrl-X"),
                    ("Copy", "Ctrl-C"),
                    ("Paste", "Ctrl-V"),
                    ("Export Selection", "Ctrl-E"),

                    ("New World", "Ctrl-N"),
                    ("Quick Load", "Ctrl-L"),
                    ("Open", "Ctrl-O"),
                    ("Save", "Ctrl-S"),
                    ("Reload World", "Ctrl-R"),
                    ("Close World", "Ctrl-W"),
                    ("World Info", "Ctrl-I"),
                    ("Quit", "Ctrl-Q"),

                    ("Take a Screenshot", "F6"),
                    ("Debug Overlay", "0"),
                    ("Fast Nudge", "None"),
                    ("Fast Increment Modifier", "Ctrl")
                ],
                "Numpad": [
                    ("Forward", "[8]"),
                    ("Back", "[5]"),
                    ("Left", "[4]"),
                    ("Right", "[6]"),
                    ("Up", "[7]"),
                    ("Down", "[1]"),
                    ("Brake", "[0]"),

                    ("Pan Up", "I"),
                    ("Pan Down", "K"),
                    ("Pan Left", "J"),
                    ("Pan Right", "L"),
                    ("Toggle View", "Tab"),
                    ("Goto Panel", "Ctrl-G"),
                    ("View Distance", "Ctrl-F"),
                    ("Toggle Renderer", "Ctrl-M"),
                    ("Fly Mode", "None"),

                    ("Increase Reach", "Scroll Up"),
                    ("Decrease Reach", "Scroll Down"),
                    ("Reset Reach", "Button 3"),
                    ("Show Block Info", "Alt"),
                    ("Pick Block", "Alt"),
                    ("Snap Clone to Axis", "Ctrl"),
                    ("Long-Distance Mode", "Alt-Z"),
                    ("Blocks-Only Modifier", "Alt"),

                    ("Rotate (Brush)", "[-]"),
                    ("Roll (Brush)", "[*]"),
                    ("Increase Brush", "[+]"),
                    ("Decrease Brush", "[/]"),
                    ("Brush Line Tool", "Z"),

                    ("Rotate (Clone)", "[-]"),
                    ("Roll (Clone)", "[+]"),
                    ("Flip", "[/]"),
                    ("Mirror", "[*]"),

                    ("Replace Shortcut", "R"),
                    ("Swap", "[.]"),

                    ("Select Chunks", "Z"),
                    ("Deselect Chunks", "Alt"),

                    ("Delete Blocks", "Delete"),
                    ("Select All", "Ctrl-A"),
                    ("Deselect", "Ctrl-D"),
                    ("Undo", "Ctrl-Z"),
                    ("Redo", "Ctrl-Y"),
                    ("Cut", "Ctrl-X"),
                    ("Copy", "Ctrl-C"),
                    ("Paste", "Ctrl-V"),
                    ("Export Selection", "Ctrl-E"),

                    ("New World", "Ctrl-N"),
                    ("Quick Load", "Ctrl-L"),
                    ("Open", "Ctrl-O"),
                    ("Save", "Ctrl-S"),
                    ("Reload World", "Ctrl-R"),
                    ("Close World", "Ctrl-W"),
                    ("World Info", "Ctrl-I"),
                    ("Quit", "Ctrl-Q"),

                    ("Take a Screenshot", "F6"),
                    ("Debug Overlay", "0"),
                    ("Fast Nudge", "None"),
                    ("Fast Increment Modifier", "Ctrl")
                ],
                "WASD Old": [
                    ("Forward", "W"),
                    ("Back", "S"),
                    ("Left", "A"),
                    ("Right", "D"),
                    ("Up", "Q"),
                    ("Down", "Z"),
                    ("Brake", "Space"),

                    ("Pan Up", "I"),
                    ("Pan Down", "K"),
                    ("Pan Left", "J"),
                    ("Pan Right", "L"),
                    ("Toggle View", "Tab"),
                    ("Goto Panel", "Ctrl-G"),
                    ("View Distance", "Ctrl-F"),
                    ("Toggle Renderer", "Ctrl-M"),
                    ("Fly Mode", "None"),

                    ("Increase Reach", "Scroll Up"),
                    ("Decrease Reach", "Scroll Down"),
                    ("Reset Reach", "Button 3"),
                    ("Show Block Info", "Alt"),
                    ("Pick Block", "Alt"),
                    ("Snap Clone to Axis", "Shift"),
                    ("Long-Distance Mode", "Alt-Z"),
                    ("Blocks-Only Modifier", "Alt"),

                    ("Rotate (Brush)", "E"),
                    ("Roll (Brush)", "G"),
                    ("Increase Brush", "R"),
                    ("Decrease Brush", "F"),
                    ("Brush Line Tool", "Shift"),

                    ("Rotate (Clone)", "E"),
                    ("Roll (Clone)", "R"),
                    ("Flip", "F"),
                    ("Mirror", "G"),

                    ("Replace Shortcut", "R"),
                    ("Swap", "X"),

                    ("Select Chunks", "Ctrl"),
                    ("Deselect Chunks", "Shift"),

                    ("Delete Blocks", "Delete"),
                    ("Select All", "Ctrl-A"),
                    ("Deselect", "Ctrl-D"),
                    ("Undo", "Ctrl-Z"),
                    ("Redo", "Ctrl-Y"),
                    ("Cut", "Ctrl-X"),
                    ("Copy", "Ctrl-C"),
                    ("Paste", "Ctrl-V"),
                    ("Export Selection", "Ctrl-E"),

                    ("New World", "Ctrl-N"),
                    ("Quick Load", "Ctrl-L"),
                    ("Open", "Ctrl-O"),
                    ("Save", "Ctrl-S"),
                    ("Reload World", "Ctrl-R"),
                    ("Close World", "Ctrl-W"),
                    ("World Info", "Ctrl-I"),
                    ("Quit", "Ctrl-Q"),

                    ("Take a Screenshot", "F6"),
                    ("Debug Overlay", "0"),
                    ("Fast Nudge", "Shift"),
                    ("Fast Increment Modifier", "Shift")
                ]}

    selectedKeyIndex = 0

    def __init__(self, mcedit):
        Dialog.__init__(self)
        #.#
        spacing = 0
        keyConfigTable = albow.TableView(nrows=30,
            columns=[albow.TableColumn("Command", 200, "l"), albow.TableColumn("Assigned Key", 150, "r")])
        keyConfigTable.num_rows = lambda: len(self.keyConfigKeys)
        keyConfigTable.row_data = self.getRowData
        keyConfigTable.row_is_selected = lambda x: x == self.selectedKeyIndex
        keyConfigTable.click_row = self.selectTableRow
        keyConfigTable.key_down = self.key_down
        keyConfigTable.key_up = self.key_up
        #.#
        self.changes = {}
        self.changesNum = False
        self.enter = 0
        self.root = None
        self.editor = None
        tableWidget = albow.Widget()
        tableWidget.add(keyConfigTable)
        tableWidget.shrink_wrap()

        self.keyConfigTable = keyConfigTable

        buttonRow = (albow.Button("Assign Key...", action=self.askAssignSelectedKey),
                    albow.Button("Done", action=self.done), albow.Button("Cancel", action=self.cancel))

        buttonRow = albow.Row(buttonRow)

        resetToDefaultRow = albow.Row((albow.Button("Reset to default", action=self.resetDefault),))

        choiceButton = mceutils.ChoiceButton(["WASD", "Arrows", "Numpad", "WASD Old"], choose=self.choosePreset)
        if config.keys.forward.get() == "Up":
            choiceButton.selectedChoice = "Arrows"
        elif config.keys.forward.get() == "[8]":
            choiceButton.selectedChoice = "Numpad"
        elif config.keys.brake.get() == "Space":
            choiceButton.selectedChoice = "WASD Old"

        self.oldChoice = choiceButton.selectedChoice

        choiceRow = albow.Row((albow.Label("Presets: "), choiceButton))
        self.choiceButton = choiceButton

        col = albow.Column((tableWidget, choiceRow, buttonRow, resetToDefaultRow), spacing=spacing, margin=0)
        self.add(col)
        self.shrink_wrap()

    def presentControls(self):
        self.present()
        self.oldChoice = self.choiceButton.selectedChoice

    def done(self):
        self.changesNum = False
        self.changes = {}
        config.save()

        self.editor.movements = [
            config.keys.left.get(),
            config.keys.right.get(),
            config.keys.forward.get(),
            config.keys.back.get(),
            config.keys.up.get(),
            config.keys.down.get()
        ]

        self.editor.cameraPan = [
            config.keys.panLeft.get(),
            config.keys.panRight.get(),
            config.keys.panUp.get(),
            config.keys.panDown.get()
        ]

        self.dismiss()

    def choosePreset(self):
        preset = self.choiceButton.selectedChoice
        keypairs = self.presets[preset]
        for configKey, k in keypairs:
            oldOne = config.keys[config.convert(configKey)].get()
            if k != oldOne:
                self.changesNum = True
                if configKey not in self.changes:
                    self.changes[configKey] = oldOne
                config.keys[config.convert(configKey)].set(k)

    def getRowData(self, i):
        if self.root is None:
            self.root = self.get_root()
        if self.editor is None:
            self.editor = self.root.editor
        configKey = self.keyConfigKeys[i]
        if self.isConfigKey(configKey):
            key = config.keys[config.convert(configKey)].get()
            try:
                key = self.editor.different_keys[key]
            except:
                pass

            if configKey in self.otherNames.keys():
                configKey = self.otherNames[configKey]

        else:
            key = ""
        return configKey, key

    @staticmethod
    def isConfigKey(configKey):
        return not (len(configKey) == 0 or configKey[0] == "<")

    def selectTableRow(self, i, evt):
        self.selectedKeyIndex = i
        if evt.num_clicks == 2:
            self.askAssignSelectedKey()

    def resetDefault(self):
        self.choiceButton.selectedChoice = "WASD"
        self.choosePreset()

    def cancel(self):
        if self.changesNum:
            result = albow.ask("Do you want to save your changes?", ["Save", "Don't Save", "Cancel"])
            if result == "Save":
                self.done()
            elif result == "Don't Save":
                for k in self.changes.keys():
                    config.keys[config.convert(k)].set(self.changes[k])
                self.changesNum = False
                self.changes = {}
                self.choiceButton.selectedChoice = self.oldChoice
                config.save()
                self.dismiss()
        else:
            self.dismiss()

    def unbind(self):
        configKey = self.keyConfigKeys[self.selectedKeyIndex]
        if config.keys[config.convert(configKey)].get() != "None":
            self.changesNum = True
        config.keys[config.convert(configKey)].set("None")
        self.panel.dismiss()

    def key_down(self, evt):
        keyname = self.root.getKey(evt)
        if keyname == 'Escape':
            self.cancel()
        elif keyname == 'Up' and self.selectedKeyIndex > 0:
            self.selectedKeyIndex -= 1
        elif keyname == 'Down' and self.selectedKeyIndex < len(self.keyConfigKeys) - 1:
            self.selectedKeyIndex += 1
        elif keyname == 'Return':
            self.enter += 1
            self.askAssignSelectedKey()

    def key_up(self, evt):
        pass

    def askAssignSelectedKey(self):
        self.askAssignKey(self.keyConfigKeys[self.selectedKeyIndex])

    def askAssignKey(self, configKey, labelString=None):
        if not self.isConfigKey(configKey):
            self.enter = 0
            return

        panel = Panel()
        panel.bg_color = (0.5, 0.5, 0.6, 1.0)

        if labelString is None and configKey != "Fast Nudge":
            labelString = _("Press a key to assign to the action \"{0}\"\n\nPress ESC to cancel.").format(configKey)
        elif labelString is None:
            labelString = _("Press a key to assign to the action \"{0}\"\nNo key means right click to fast nudge.\nPress ESC to cancel.").format(configKey)
        label = albow.Label(labelString)
        unbind_button = Button("Press to unbind", action=self.unbind)
        column = Column((label, unbind_button))
        panel.add(column)
        panel.shrink_wrap()

        def panelKeyUp(evt):
            keyname = self.root.getKey(evt)
            panel.dismiss(keyname)

        def panelMouseUp(evt):
            button = remapMouseButton(evt.button)
            if button == 3:
                keyname = "Button 3"
            elif button == 4:
                keyname = "Scroll Up"
            elif button == 5:
                keyname = "Scroll Down"
            elif button == 6:
                keyname = "Button 4"
            elif button == 7:
                keyname = "Button 5"
            if button > 2:
                panel.dismiss(keyname)

        panel.key_up = panelKeyUp
        panel.mouse_up = panelMouseUp

        self.panel = panel
        keyname = panel.present()
        if type(keyname) is bool:
            return True
        if keyname == "Return" and self.enter == 1:
            self.enter = 0
            self.askAssignKey(configKey)
            return True

        self.enter = 0
        if keyname != "Escape" and keyname not in ["Alt-F4","F1","F2","F3","F4","F5","1","2","3","4","5","6","7","8","9","Ctrl-Alt-F9","Ctrl-Alt-F10"]:
            if "Modifier" in configKey and keyname != "Ctrl" and keyname != "Alt" and keyname != "Shift":
                self.askAssignKey(configKey,
                                    _("{0} is not a modifier. Press a new key.\n\nPress ESC to cancel.")
                                    .format(keyname))
                return True
            if configKey in ['Down','Up','Back','Forward','Left','Right','Pan Down','Pan Up','Pan Left','Pan Right']:
                if 'Ctrl' in keyname or '-' in keyname:
                    self.askAssignKey(configKey,
                                    "Movement keys can't use Ctrl or be with modifiers. Press a new key.\n\nPress ESC to cancel.")
                    return True
            filter_keys = [i for (i, j) in config.config._sections["Filter Keys"].items() if j == keyname]
            if filter_keys:
                self.askAssignKey(configKey,
                                    _("Can't bind. {0} is already used by the \"{1}\" filter.\n Press a new key.\n\nPress ESC to cancel.").format(keyname, filter_keys[0]))
                return True
            oldkey = config.keys[config.convert(configKey)].get()
            config.keys[config.convert(configKey)].set(keyname)
            if configKey not in self.changes:
                self.changes[configKey] = oldkey
            self.changesNum = True
        elif keyname != "Escape":
            self.askAssignKey(configKey,
                                    _("You can't use the key {0}. Press a new key.\n\nPress ESC to cancel.")
                                    .format(keyname))
            return True

        else:
            return True
