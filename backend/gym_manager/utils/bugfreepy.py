import colorama
# from termcolor import colored

# 初始化colorama
colorama.init()


def bug_free_str(type='buddha'):  
    buddha_text = r"""  
                    _ooOoo_
                   o8888888o
                   88" . "88
                   (| -_- |)
                    O\ = /O
                ____/`---'\____
              .   ' \\| |// `.
               / \\||| : |||// \
             / _||||| -:- |||||- \
               | | \\\ - /// | |
             | \_| ''\---/'' | |
              \ .-\__ `-` ___/-. /
           ___`. .' /--.--\ `. . __
        ."" '< `.___\_<|>_/___.' >'"".
       | | : `- \`.;`\ _ /`;.`/ - ` : | |
         \ \ `-. \_ __\ /__ _/ .-` / /
 ======`-.____`-.___\_____/___.-`____.-'======
                    `=---='

 .............................................
          佛祖保佑             永无BUG
  佛曰:
          写字楼里写字间，写字间里程序员；
          程序人员写程序，又拿程序换酒钱。
          酒醒只在网上坐，酒醉还来网下眠；
          酒醉酒醒日复日，网上网下年复年。
          但愿老死电脑间，不愿鞠躬老板前；
          奔驰宝马贵者趣，公交自行程序员。
          别人笑我忒疯癫，我笑自己命太贱；
          不见满街漂亮妹，哪个归得程序员？  
    """ 
    mythical_animals_text = r"""
      ┌─┐       ┌─┐
   ┌──┘ ┴───────┘ ┴──┐
   │                 │
   │       ───       │
   │   >        <    │
   │                 │
   │   ...  ⌒  ...   │
   │                 │
   └───┐         ┌───┘
       │         │
       │         │
       │         │
       │         └──────────────┐
       │                        │
       │                        ├─┐
       │                        ┌─┘
       │                        │
       └─┐  ┐  ┌───────┬──┐  ┌──┘
         │ ─┤ ─┤       │ ─┤ ─┤
         └──┴──┘       └──┴──┘
                神兽保佑
               代码无BUG!
    """
    if type == 'buddha': 
        return buddha_text
    elif type == 'mythical_animals':
        return mythical_animals_text
    else:
        return buddha_text



def get_gradient_text(text, start_color, end_color):
    def hex2RGB(hex):
        return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))

    def interpolate(start, end, factor):
        return int(start + (end - start) * factor)
    
    def get_color_code(r, g, b):
        return f'\033[38;2;{r};{g};{b}m'
    
    # 将颜色转换为RGB值
    start_r, start_g, start_b = hex2RGB(start_color)
    end_r, end_g, end_b = hex2RGB(end_color)

    gradient_text = ""

    for i, char in enumerate(text):
        factor = i / (len(text) - 1) if len(text) > 1 else 0
        r = interpolate(start_r, end_r, factor)
        g = interpolate(start_g, end_g, factor)
        b = interpolate(start_b, end_b, factor)

        # 生成渐变色字符
        color_code = get_color_code(r, g, b)
        gradient_text += f"{color_code}{char}"
    
    # 重置颜色
    gradient_text += colorama.Style.RESET_ALL
    return gradient_text

def gradient_texts(texts, start_color, end_color):
    max_length = max([len(text) for text in texts])
    gradient_texts = []
    for text in texts:
        gradient_texts.append(get_gradient_text(text.ljust(max_length), start_color, end_color))
    return gradient_texts

def get_bug_free_gradient_texts(type='buddha', start_color="FF7EC7", end_color="FFED46"):
    bug_free_texts = bug_free_str(type).splitlines()  # 按行分割
    gt = gradient_texts(bug_free_texts, start_color, end_color)
    return gt

def print_bug_free_gradient_texts(type='buddha', start_color="FF7EC7", end_color="FFED46"):
    gts = get_bug_free_gradient_texts(type, start_color, end_color)
    for gt in gts:
        print(gt)
        
# if __name__ == "__main__":
#     print_bug_free_gradient_texts('buddha', "FF7EC7", "FFED46")
#     print()
#     print_bug_free_gradient_texts('mythical_animals', "FF7EC7", "FFED46")