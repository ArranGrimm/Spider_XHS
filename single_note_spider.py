from xhs_utils.common_util import init
from main import Data_Spider

if __name__ == '__main__':
    cookies_str, base_path = init()  # 读取 .env 里的 cookie、输出目录
    if not cookies_str:
        raise RuntimeError('请先在 .env 中配置 COOKIES=完整的登录 cookie 字符串')
    if 'a1=' not in cookies_str:
        raise RuntimeError('当前 cookie 缺少 a1 字段，需重新从浏览器复制完整 cookie（含 a1）')
    spider = Data_Spider()

    note_url = 'https://www.xiaohongshu.com/explore/68dc8ce40000000003023d20?xsec_token=ABMsKNXHUvcCka-C2rkcPm12xJeZ6eOAI6xEOGdvW-vl8=&xsec_source=pc_user&source=web_user_page'

    success, msg, note_info = spider.spider_note(note_url, cookies_str)
    if not success:
        raise RuntimeError(msg)

    spider.spider_some_note(
        notes=[note_url],
        cookies_str=cookies_str,
        base_path=base_path,
        save_choice='media-image',       # all / media / media-image / media-video / excel
        excel_name='single_note' # save_choice 含 all 或 excel 时必填
    )