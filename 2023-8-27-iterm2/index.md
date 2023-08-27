# iTerm2 的常用配置 -- iTerm2+ZSH 最好的终端工具


## 1 背景

作为一名程序员，每天用终端工具的机会太多了，一个好的终端工具能很大程度提高开发效率，同时也能改善心情🐶。 

<br>

可能一些公司是内部有自研的终端工具，但对于普通用户来说，我个人目前觉得iTerm2 + ZSH 是最好的组合工具了，这篇文章是总结我个人使用时候的心得，也是参考网上的一些资料。

<br>

## 2 系统环境

我的电脑是MAC的，配置如下：

> `chip: Apple M1 Pro`
>
> `OS: Ventura 13.4`

<br>

## 3 安装手册

其实我基本上是按照下面的两个链接来安装和配置的。

*   <https://zhuanlan.zhihu.com/p/550022490>
*   <https://www.jianshu.com/p/40a13bf42f44>

<br>

最后的效果是这样：

<img src="https://cdn.jsdelivr.net/gh/yeliansong/github-blog-PIC/blog-images/WX20230827-191733.png" style="zoom:200%;" />

`基本上是安装ZSH、配置iTerm2 的主题、设置颜色、字体、配置VIM 编辑器这些。`
<br>

步骤按照这两个链接来，我就不细说了。

<br>

## 4 补充

> **`PicGo 图床工具`**

这个可以说是写markdown 必备的神器，我之前是用的`ipic`，被狠狠的坑了一把，它是默认上传到微博图床，但后面微博图床被禁了，之前上传的图片全部不能访问。故这次选择了PicGo 图床工具，支持多种图床，我搭配的是`github` 的图床加上`jsDelivr` 免费的CDN 加速工具，非常好用。

<br>

`配置的参考链接如下`：[https://zhuanlan.zhihu.com/p/353775844](https://zhuanlan.zhihu.com/p/353775844)

<br>

`也记录一个使用PicGO 图床工具的，安装在mac 上可能出现安装包damage的问题，可以在终端上run 下这个命令`：

```bash
sudo xattr -d com.apple.quarantine "/Applications/PicGo.app"
```

<br>

> **`我的iTerm2 配置文件`**

下面这个可以字节拷贝，直接导入用。

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


