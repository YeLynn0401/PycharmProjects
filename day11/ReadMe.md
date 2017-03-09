* 示例
<pre><code>
>>:run "df -h" --host 192.168.3.55 10.4.3.4
task id: 45334
>>: check_task 45334
>>:
</code></pre>

* check_task 只可查询一次

* server端自动获取本机ip， --host 后ip地址中含有本机ip才执行命令，不含则忽略