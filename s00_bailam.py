#region debai
"""
--- ma debai / id
get_name_in_email(email_list)

--- nopbai
00 fork tu bainopmau tren replit tu trang web duoiday 
   https://replit.com/@NamG1/bainopmau2310121414emailhople

01 lam bai vao tep s00_bailam.py, chay Run de co ketqua tatca la 1
02a tao github repo, mo kiemtra tep s00_bailam.py, va lay diachi/url aka githubrepourl

02b dan diachi githubrepourl tu trang web duoiday
    https://forms.gle/11knZyUvwRzU7SvL6

--- debai / problem
Viết hàm 
  get_name_in_email(email_list)
trả về tên tài khoản trong email 
Nếu email không hợp lệ tả về ERROR invaid email

--- vidu mau / testcase
Khi chay voi input                                        | Ketqua output
--------------------------------------------------------- | -----------------
get_name_in_email(['ai-btx@gmail.com'])                   | ['ai-btx']
get_name_in_email(['user1@gmail.com', 'user2@gmail.com']) | ['user1', 'user2']
get_name_in_email([])                                     | []
get_name_in_email(['abb#ccc'])                            | ['ERROR invaid email']
get_name_in_email([None])                                 | ['ERROR invaid email']
get_name_in_email([None, 'abb#ccc'])                      | ['ERROR invaid email', 'ERROR invaid email']
"""
#endregion debai

#region bailam
def get_name_in_email(email_list):
  if(email_list == None or len(email_list) == 0):
    return []
  ans =[None]*len(email_list)
  de = 0
  for em in email_list:
    if(em == None or em == ''):
      ans[de] = 'ERROR invaid email'
    elif(em.find('@') == -1):
      ans[de] = 'ERROR invaid email'
    else:
      ans = [em.split('@')[0] for em in email_list]
    de += 1
  return ans
#endregion bailam
