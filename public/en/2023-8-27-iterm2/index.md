# Common configuration of iTerm2 -- iTerm2+ZSH the best terminal tool


## 1 background

As a programmer, there are too many opportunities to use terminal tools every day. A good terminal tool can greatly improve development efficiency and improve mood🐶.

<br>

Maybe some companies have self-developed terminal tools internally, but for ordinary users, I personally think that iTerm2 + ZSH is the best combined tool. This article summarizes my personal experience when using it, and also refers to the Internet. some documents.

<br>

## 2 System environment

My computer is a MAC, the configuration is as follows:

> `chip: Apple M1 Pro`
>
> `OS: Ventura 13.4`

<br>

## 3 Installation Manual

In fact, I basically followed the two links below to install and configure.

* <https://zhuanlan.zhihu.com/p/550022490>
* <https://www.jianshu.com/p/40a13bf42f44>

<br>

The final effect is this:

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/WX20230827-191733.png" style="zoom:200%;" />

`Basically install ZSH, configure iTerm2 theme, set colors, fonts, configure VIM editor and so on. `
<br>

The steps follow these two links, so I won't go into details.

<br>

## 4 Supplements

> **`PicGo Image Bed Tool`**

This can be said to be a necessary artifact for writing markdown. I used `ipic` before, and I was severely cheated. It was uploaded to Weibo by default, but later Weibo was banned. Before All uploaded pictures cannot be accessed. So this time I chose the PicGo image bed tool, which supports a variety of image tables. I used the `github` image bed and the free CDN acceleration tool of `jsDelivr`, which is very easy to use.

<br>

`The reference link for configuration is as follows`: [https://zhuanlan.zhihu.com/p/353775844](https://zhuanlan.zhihu.com/p/353775844)

<br>

`Also record a use of the PicGO image bed tool, there may be a problem with the installation package damage when installed on a mac, you can run this command on the terminal`:

```bash
sudo xattr -d com.apple.quarantine "/Applications/PicGo.app"
```

<br>

> **`My iTerm2 Configuration File`**

The following can be byte copied and imported directly.

```json
{
  "ASCII Ligatures" : false,
  "Working Directory" : "\/Users\/bytedance",
  "Prompt Before Closing 2" : false,
  "Selected Text Color" : {
    "Green Component" : 0.56244754791259766,
    "Red Component" : 0.47797361016273499,
    "Blue Component" : 0.55732053518295288
  },
  "Rows" : 43,
  "Ansi 11 Color" : {
    "Green Component" : 0.49430075287818909,
    "Red Component" : 0.69710838794708252,
    "Blue Component" : 0.1584954559803009
  },
  "Use Italic Font" : true,
  "Foreground Color" : {
    "Green Component" : 0.75921261310577393,
    "Red Component" : 0.61000990867614746,
    "Blue Component" : 0.7630731463432312
  },
  "Right Option Key Sends" : 0,
  "Show Status Bar" : false,
  "Character Encoding" : 4,
  "Selection Color" : {
    "Green Component" : 0.21576285362243652,
    "Red Component" : 0,
    "Blue Component" : 0.28167051076889038
  },
  "Mouse Reporting" : true,
  "Ansi 4 Color" : {
    "Green Component" : 0.46265947818756104,
    "Red Component" : 0.12754884362220764,
    "Blue Component" : 0.78231418132781982
  },
  "Non-ASCII Anti Aliased" : true,
  "Sync Title" : false,
  "Disable Window Resizing" : true,
  "Description" : "Default",
  "Close Sessions On End" : true,
  "Jobs to Ignore" : [
    "rlogin",
    "ssh",
    "slogin",
    "telnet"
  ],
  "Scrollback Lines" : 1000,
  "Status Bar Layout" : {
    "components" : [
      {
        "class" : "iTermStatusBarCPUUtilizationComponent",
        "configuration" : {
          "knobs" : {
            "base: priority" : 5,
            "base: compression resistance" : 1
          },
          "layout advanced configuration dictionary value" : {
            "auto-rainbow style" : 0,
            "algorithm" : 0,
            "remove empty components" : false
          }
        }
      },
      {
        "class" : "iTermStatusBarMemoryUtilizationComponent",
        "configuration" : {
          "knobs" : {
            "base: priority" : 5,
            "base: compression resistance" : 1
          },
          "layout advanced configuration dictionary value" : {
            "auto-rainbow style" : 0,
            "algorithm" : 0,
            "remove empty components" : false
          }
        }
      }
    ],
    "advanced configuration" : {
      "remove empty components" : false,
      "font" : ".AppleSystemUIFont 12",
      "algorithm" : 0,
      "auto-rainbow style" : 0
    }
  },
  "Brighten Bold Text" : true,
  "Flashing Bell" : false,
  "Cursor Guide Color" : {
    "Red Component" : 0.70214027166366577,
    "Color Space" : "sRGB",
    "Blue Component" : 1,
    "Alpha Component" : 0.25,
    "Green Component" : 0.92681378126144409
  },
  "BM Growl" : true,
  "Ansi 3 Color" : {
    "Green Component" : 0.46751424670219421,
    "Red Component" : 0.64746475219726562,
    "Blue Component" : 0.023484811186790466
  },
  "Use Non-ASCII Font" : false,
  "Link Color" : {
    "Red Component" : 0.030515776947140694,
    "Color Space" : "sRGB",
    "Blue Component" : 0.62457275390625,
    "Alpha Component" : 1,
    "Green Component" : 0.32110351021536249
  },
  "Shortcut" : "",
  "Background Image Location" : "",
  "Bold Color" : {
    "Green Component" : 0.83450067043304443,
    "Red Component" : 0.70913255214691162,
    "Blue Component" : 0.82687115669250488
  },
  "Unlimited Scrollback" : false,
  "Custom Command" : "No",
  "Title Components" : 2,
  "Keyboard Map" : {
    "0xf700-0x260000" : {
      "Text" : "[1;6A",
      "Action" : 10
    },
    "0x37-0x40000" : {
      "Text" : "0x1f",
      "Action" : 11
    },
    "0x32-0x40000" : {
      "Text" : "0x00",
      "Action" : 11
    },
    "0xf709-0x20000" : {
      "Text" : "[17;2~",
      "Action" : 10
    },
    "0xf70c-0x20000" : {
      "Text" : "[20;2~",
      "Action" : 10
    },
    "0xf729-0x20000" : {
      "Text" : "[1;2H",
      "Action" : 10
    },
    "0xf72b-0x40000" : {
      "Text" : "[1;5F",
      "Action" : 10
    },
    "0xf705-0x20000" : {
      "Text" : "[1;2Q",
      "Action" : 10
    },
    "0xf703-0x260000" : {
      "Text" : "[1;6C",
      "Action" : 10
    },
    "0xf700-0x220000" : {
      "Text" : "[1;2A",
      "Action" : 10
    },
    "0xf701-0x280000" : {
      "Text" : "0x1b 0x1b 0x5b 0x42",
      "Action" : 11
    },
    "0x38-0x40000" : {
      "Text" : "0x7f",
      "Action" : 11
    },
    "0x33-0x40000" : {
      "Text" : "0x1b",
      "Action" : 11
    },
    "0xf703-0x220000" : {
      "Text" : "[1;2C",
      "Action" : 10
    },
    "0xf701-0x240000" : {
      "Text" : "[1;5B",
      "Action" : 10
    },
    "0xf70d-0x20000" : {
      "Text" : "[21;2~",
      "Action" : 10
    },
    "0xf702-0x260000" : {
      "Text" : "[1;6D",
      "Action" : 10
    },
    "0xf729-0x40000" : {
      "Text" : "[1;5H",
      "Action" : 10
    },
    "0xf706-0x20000" : {
      "Text" : "[1;2R",
      "Action" : 10
    },
    "0x34-0x40000" : {
      "Text" : "0x1c",
      "Action" : 11
    },
    "0xf700-0x280000" : {
      "Text" : "0x1b 0x1b 0x5b 0x41",
      "Action" : 11
    },
    "0x2d-0x40000" : {
      "Text" : "0x1f",
      "Action" : 11
    },
    "0xf70e-0x20000" : {
      "Text" : "[23;2~",
      "Action" : 10
    },
    "0xf702-0x220000" : {
      "Text" : "[1;2D",
      "Action" : 10
    },
    "0xf703-0x280000" : {
      "Text" : "0x1b 0x1b 0x5b 0x43",
      "Action" : 11
    },
    "0xf700-0x240000" : {
      "Text" : "[1;5A",
      "Action" : 10
    },
    "0xf707-0x20000" : {
      "Text" : "[1;2S",
      "Action" : 10
    },
    "0xf70a-0x20000" : {
      "Text" : "[18;2~",
      "Action" : 10
    },
    "0x35-0x40000" : {
      "Text" : "0x1d",
      "Action" : 11
    },
    "0xf70f-0x20000" : {
      "Text" : "[24;2~",
      "Action" : 10
    },
    "0xf703-0x240000" : {
      "Text" : "[1;5C",
      "Action" : 10
    },
    "0xf701-0x260000" : {
      "Text" : "[1;6B",
      "Action" : 10
    },
    "0xf702-0x280000" : {
      "Text" : "0x1b 0x1b 0x5b 0x44",
      "Action" : 11
    },
    "0xf72b-0x20000" : {
      "Text" : "[1;2F",
      "Action" : 10
    },
    "0x36-0x40000" : {
      "Text" : "0x1e",
      "Action" : 11
    },
    "0xf708-0x20000" : {
      "Text" : "[15;2~",
      "Action" : 10
    },
    "0xf701-0x220000" : {
      "Text" : "[1;2B",
      "Action" : 10
    },
    "0xf70b-0x20000" : {
      "Text" : "[19;2~",
      "Action" : 10
    },
    "0xf702-0x240000" : {
      "Text" : "[1;5D",
      "Action" : 10
    },
    "0xf704-0x20000" : {
      "Text" : "[1;2P",
      "Action" : 10
    }
  },
  "Ansi 14 Color" : {
    "Green Component" : 0.70167088508605957,
    "Red Component" : 0,
    "Blue Component" : 0.62018769979476929
  },
  "Ansi 2 Color" : {
    "Green Component" : 0.7455558180809021,
    "Red Component" : 0.42339208722114563,
    "Blue Component" : 0.42409399151802063
  },
  "Send Code When Idle" : false,
  "ASCII Anti Aliased" : true,
  "Tags" : [

  ],
  "Ansi 9 Color" : {
    "Green Component" : 0.084504462778568268,
    "Red Component" : 0.95941102504730225,
    "Blue Component" : 0.23225757479667664
  },
  "Use Bold Font" : true,
  "Silence Bell" : false,
  "Ansi 12 Color" : {
    "Green Component" : 0.55553519725799561,
    "Red Component" : 0.091996639966964722,
    "Blue Component" : 0.78393226861953735
  },
  "Window Type" : 0,
  "Use Bright Bold" : false,
  "Cursor Text Color" : {
    "Green Component" : 0.15575926005840302,
    "Red Component" : 0,
    "Blue Component" : 0.19370138645172119
  },
  "Default Bookmark" : "No",
  "Cursor Color" : {
    "Green Component" : 0.29334646463394165,
    "Red Component" : 0.95475113391876221,
    "Blue Component" : 0
  },
  "Ansi 1 Color" : {
    "Green Component" : 0.10840655118227005,
    "Red Component" : 0.81926977634429932,
    "Blue Component" : 0.14145714044570923
  },
  "Name" : "Default",
  "Blinking Cursor" : false,
  "Guid" : "8798F8B8-6F02-4D92-9C09-0970CA99189E",
  "Idle Code" : 0,
  "Ansi 10 Color" : {
    "Green Component" : 0.93699550628662109,
    "Red Component" : 0.31744870543479919,
    "Blue Component" : 0.51931029558181763
  },
  "Ansi 8 Color" : {
    "Green Component" : 0.39142724871635437,
    "Red Component" : 0,
    "Blue Component" : 0.53505516052246094
  },
  "Badge Color" : {
    "Red Component" : 1,
    "Color Space" : "sRGB",
    "Blue Component" : 0,
    "Alpha Component" : 0.5,
    "Green Component" : 0.14910030364990234
  },
  "Ambiguous Double Width" : false,
  "Cursor Type" : 1,
  "Ansi 0 Color" : {
    "Green Component" : 0.15575926005840302,
    "Red Component" : 0,
    "Blue Component" : 0.19370138645172119
  },
  "Blur" : false,
  "Normal Font" : "MesloLGLForPowerline-Regular 11",
  "Vertical Spacing" : 1,
  "Use Underline Color" : false,
  "Ansi 7 Color" : {
    "Green Component" : 0.89001238346099854,
    "Red Component" : 0.91611063480377197,
    "Blue Component" : 0.79781103134155273
  },
  "Command" : "",
  "Terminal Type" : "xterm-256color",
  "Horizontal Spacing" : 1,
  "Option Key Sends" : 0,
  "Blink Allowed" : false,
  "Minimum Contrast" : 0,
  "Ansi 15 Color" : {
    "Green Component" : 0.95794391632080078,
    "Red Component" : 0.98943418264389038,
    "Blue Component" : 0.86405980587005615
  },
  "Unicode Version" : 9,
  "Ansi 6 Color" : {
    "Green Component" : 0.57082360982894897,
    "Red Component" : 0.14679534733295441,
    "Blue Component" : 0.52502274513244629
  },
  "Transparency" : 0,
  "Initial Text" : "",
  "Background Color" : {
    "Green Component" : 0.11783610284328461,
    "Red Component" : 0,
    "Blue Component" : 0.15170273184776306
  },
  "Screen" : -1,
  "Non Ascii Font" : "Monaco 12",
  "Ansi 13 Color" : {
    "Green Component" : 0.30289158225059509,
    "Red Component" : 0.88624399900436401,
    "Blue Component" : 0.55838865041732788
  },
  "Columns" : 186,
  "Show Timestamps" : 1,
  "Visual Bell" : true,
  "Custom Directory" : "No",
  "Thin Strokes" : 4,
  "Ansi 5 Color" : {
    "Green Component" : 0.10802463442087173,
    "Red Component" : 0.77738940715789795,
    "Blue Component" : 0.43516635894775391
  }
}
```






