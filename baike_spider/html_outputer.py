#coding:utf-8
'''
Created on 2017-5-28
@author: ZXQ20
'''


class HtmlOutputer(object): 
    def __init__(self): 
        self.datas = [] 
    def collect_data(self,data): 
        if data is None: 
            return 
        self.datas.append(data) 
    def output_html(self): 
        fout = open("output.html","w") 
        fout.write("<html>") 
        fout.write("<body>") 
        fout.write("<table>") 
        for data in self.datas: 
            fout.write("<tr>") 
            fout.write(r"<td width='25%%'>%s</td>"%data["url"]) 
            fout.write("<td width='5%%'>%s</td>"%data["title"].encode("utf-8")) 
            fout.write("<td width='70%%'>%s</td>"%data["summary"].encode("utf-8")) 
            fout.write("</tr>") 
        fout.write("</table>") 
        fout.write("</body>") 
        fout.write("</html>")
