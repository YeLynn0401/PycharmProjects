/**
 * Created by john on 2017/3/21.
 */
/* user-cart cart-recommend.js Date:2017-03-10 10:11:49 */
window.pageConfig.protocol = "https:" == document.location.protocol ? "//" : "http://";
function logRecommend(a) {
    if (a) {
        var b = new Image;
        a = a.replace("http://", pageConfig.protocol);
        var c = a + "&m=UA-J2011-1&ref=" + encodeURIComponent(document.referrer) + "&random=" + Math.random();
        b.setAttribute("src", c)
    }
}
var Grecommend = {
    init: function (a, b, c, d, e, f) {
        this.sku = a, this.rid = b, this.locId = c, this.onLoad = e || function () {
            }, this.pin = readCookie("pin"), this.pid = null === c ? 1 : c.split("-")[0], this.el = d, this.callback = f || function () {
            };
        var g = readCookie("__jda");
        this.uuid = g ? "-" == g.split(".")[1] ? -1 : g.split(".")[1] : -1, this.get()
    }, get: function () {
        var b = {
            p: this.rid,
            skus: this.sku,
            lid: this.pid,
            lim: 12,
            uuid: this.uuid,
            ck: "ipLoction",
            ec: "utf-8",
            callback: "Grecommend.set"
        };
        this.pin && (b.pin = this.pin), 906005 == this.rid && (b.ck = "pin,aview,pinId,lighting"), 205e3 === this.rid && delete b.ck, $.ajax({
            url: "//mixer.jd.com/diviner?" + decodeURIComponent($.param(b)),
            dataType: "script",
            cache: !0
        })
    }, set: function (a) {
        var b = "";
        906005 == this.rid && (b = ' clstag="pageclick|keycount|cart__201503041|3"', clstagsImg = ' clstag="pageclick|keycount|201601152|20"', clstagsName = ' clstag="pageclick|keycount|201601152|21'), 205e3 === this.rid && (b = ' clstag="pageclick|keycount|cart__201503041|1"', clstagsImg = ' clstag="pageclick|keycount|201601152|16"', clstagsName = ' clstag="pageclick|keycount|201601152|17"');
        var c = '<div class="goods-list-tab"><a href="#none" class="s-item curr">&nbsp;</a><a href="#none" class="s-item">&nbsp;</a><a href="#none" class="s-item">&nbsp;</a></div>  <div class="mc c-panel-main">    <div class="goods-list c-panel">      <ul>      {for item in data}        {if item_index%4 == 0 && item_index!= 0}</ul></div><div class="goods-list c-panel hide"><ul>{/if}        <li data-clk="${item.clk}" onclick="logRecommend(\'${item.clk}\')">          <div class="item">            <div class="p-img" ' + clstagsImg + '>              <a target="_blank" href="//item.jd.com/${item.sku}.html" ><img width="160" height="160" src="${pageConfig.FN_GetImageDomain(item.sku)}n4/s160x160_${item.img}" alt="${item.t}"></a>            </div>            <div class="p-name" ' + clstagsName + '>              <a target="_blank" href="//item.jd.com/${item.sku}.html" >${item.t}</a>            </div>            <div class="p-price">              <strong><em>\uffe5</em><i>${item.jp}</i></strong>            </div>            <div class="p-btn" ' + b + '>              <a href="#none" _pid="${item.sku}" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a>            </div>          </div>        </li>      {/for}      </ul>    </div>    <div class="c-page" >      <a href="javascript:void(0)" class="c-prev">&lt;</a>       <a href="javascript:void(0)" class="c-next">&gt;</a>     </div>  </div>';
        if (a.success && a.data && a.data.length > 0) {
            var d = this.el;
            d.html(c.process(a)).parent().show(), $("#c-tabs-new .c-panel").switchable({
                type: "focus",
                navItem: "s-item",
                navSelectedClass: "curr",
                contentClass: "c-panel-main",
                mainClass: "c-panel",
                prevClass: "c-prev",
                nextClass: "c-next",
                hasPage: !0
            }), $("#c-tabs-new .goods-list .item").hover(function () {
                $(this).addClass("hover")
            }, function () {
                $(this).removeClass("hover")
            }), $(".mc", $(d)).hover(function () {
                $(".c-page", $(this)).show()
            }, function () {
                $(".c-page", $(this)).hide()
            }), this.setTrackCode(a.impr), this.onLoad(a)
        } else this.el.append('<div class="ac mt10">\u6682\u65f6\u65e0\u7ed3\u679c</div>').css({
            height: 247,
            lineHeight: "247px"
        });
        this.callback()
    }, setTrackCode: function (a) {
        var b = this.el.find("li");
        var c = this;
        var d = "&m=UA-J2011-1&ref=" + encodeURIComponent(document.referrer);
        b.each(function () {
            var a = $(this).attr("data-clk");
            $(this).bind("click", function (b) {
                var e = (b.srcElement ? b.srcElement : b.target).tagName.toUpperCase();
                ("A" === e || "IMG" === e || "SPAN" === e) && c.newImage(a + d, !0)
            })
        }), this.newImage(a + d)
    }, newImage: function (a, b, c) {
        var d = new Image;
        a = a.replace("http://", pageConfig.protocol), a = b ? a + "&random=" + Math.random() + new Date : a, d.onload = function () {
            "undefined" != typeof c && c(a)
        }, d.setAttribute("src", a)
    }
};
function someMoreRecommend(a) {
    var b = '<div class="goods-list-tab"><a href="#none" class="s-item curr">&nbsp;</a><a href="#none" class="s-item">&nbsp;</a><a href="#none" class="s-item">&nbsp;</a></div><div class="mc c-panel-main">    <div class="goods-list c-panel">      <ul>      {for item in data}        {if item_index%4 == 0 && item_index!= 0}</ul></div><div class="goods-list c-panel hide"><ul>{/if}        <li>          <div class="item">            <div class="p-img" clstag="pageclick|keycount|201601152|18">              <a target="_blank" href="//item.jd.com/${item.productId}.html" ><img width="160" height="160" src="${pageConfig.FN_GetImageDomain(item.productId)}n3/s160x160_${item.productLogo}" alt="${item.productName}"></a>            </div>            <div class="p-name" clstag="pageclick|keycount|201601152|19">              <a target="_blank" href="//item.jd.com/${item.productId}.html" >${item.productName}</a>            </div>            <div class="p-price" data-price="${item.currentPrice}">              <strong>{if item.currentPrice == -1} \u6682\u65e0\u62a5\u4ef7 {else} <em>\uffe5</em><i>${item.currentPrice}</i> {/if}</strong>            </div>            <div class="p-btn">              <a href="#none" _pid="${item.productId}" clstag="pageclick|keycount|cart__201503041|2" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a>            </div>          </div>        </li>      {/for}      </ul>    </div>    <div class="c-page" >      <a href="javascript:void(0)" class="c-prev">&lt;</a>       <a href="javascript:void(0)" class="c-next">&gt;</a>     </div>  </div>';
    $.getJSON("//passport.jd.com/loginservice.aspx?method=Login&callback=?", function (a) {
        var c = $("#favorite-products");
        a.Identity.IsAuthenticated ? $.ajax({
                url: "//t.jd.com/product/myFollowProductList.action",
                dataType: "jsonp",
                scriptCharset: "utf-8",
                success: function (a) {
                    if (a.length > 0) {
                        var d = new Array;
                        for (var e = 0; e < a.length && 12 != e; e++)d.push(a[e]);
                        c.html(b.process({data: d})).parent().show(), $("#c-tabs-new").show(), $("#favorite-products .p-price").each(function () {
                            var c = $(this).data("price");
                            -1 != c && $(this).html("<strong><em>\uffe5<em><i>" + Number(c).toFixed(2) + "</i></strong>")
                        }), $("#c-tabs-new .c-panel").switchable({
                            type: "focus",
                            navItem: "s-item",
                            navSelectedClass: "curr",
                            contentClass: "c-panel-main",
                            mainClass: "c-panel",
                            prevClass: "c-prev",
                            nextClass: "c-next",
                            hasPage: !0,
                            autoPlay: !1
                        }), $("#c-tabs-new .goods-list .item").hover(function () {
                            $(this).addClass("hover")
                        }, function () {
                            $(this).removeClass("hover")
                        }), $(".mc", $(c)).hover(function () {
                            $(".c-page", $(this)).show()
                        }, function () {
                            $(".c-page", $(this)).hide()
                        })
                    } else c.append('<div class="ac mt10">\u6682\u65f6\u65e0\u7ed3\u679c</div>').css({
                        height: 247,
                        lineHeight: "247px"
                    })
                },
                error: function () {
                    c.append('<div class="ac mt10">\u6682\u65f6\u65e0\u7ed3\u679c</div>').css({
                        height: 247,
                        lineHeight: "247px"
                    })
                }
            }) : c.append('<div class="ac mt10"><a href="javascript:void(0);" class="ftx-05 login-in">\u767b\u5f55</a>\u540e\u5c06\u663e\u793a\u60a8\u4e4b\u524d\u5173\u6ce8\u7684\u5546\u54c1</div>').css({
                height: 247,
                lineHeight: "247px"
            })
    }), Grecommend.init(a, 205e3, readCookie("ipLoc-djd"), $("#guess-products"), function (a) {
        logRecommend(a.impr)
    }, function () {
        Grecommend.init(a, 906005, readCookie("ipLoc-djd"), $("#history-products"), function (a) {
            logRecommend(a.impr)
        })
    })
}
function searchForCart(a) {
    var b = {};
    var c = "//search.jd.com/Search?keyword={keyword}&enc={enc}{additional}";
    var d = b.additinal || "";
    var e = document.getElementById(a);
    var f = e.value;
    if (f = f.replace(/^\s*(.*?)\s*$/, "$1"), f.length > 100 && (f = f.substring(0, 100)), "" != f) {
        var g = 0;
        "undefined" != typeof window.pageConfig && "undefined" != typeof window.pageConfig.searchType && (g = window.pageConfig.searchType);
        var h = "&cid{level}={cid}";
        var i = "string" == typeof b.cid ? b.cid : "";
        var j = "string" == typeof b.cLevel ? b.cLevel : "";
        var k = "string" == typeof b.ev_val ? b.ev_val : "";
        switch (g) {
            case 0:
                break;
            case 1:
                j = "-1", d += "&book=y";
                break;
            case 2:
                j = "-1", d += "&mvd=music";
                break;
            case 3:
                j = "-1", d += "&mvd=movie";
                break;
            case 4:
                j = "-1", d += "&mvd=education";
                break;
            case 5:
                var l = "&other_filters=%3Bcid1%2CL{cid1}M{cid1}[cid2]";
                switch (j) {
                    case"51":
                        h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5272");
                        break;
                    case"52":
                        h = l.replace(/\{cid1}/g, "5272"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                        break;
                    case"61":
                        h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5273");
                        break;
                    case"62":
                        h = l.replace(/\{cid1}/g, "5273"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                        break;
                    case"71":
                        h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5274");
                        break;
                    case"72":
                        h = l.replace(/\{cid1}/g, "5274"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}");
                        break;
                    case"81":
                        h = l.replace(/\[cid2]/, ""), h = h.replace(/\{cid1}/g, "5275");
                        break;
                    case"82":
                        h = l.replace(/\{cid1}/g, "5275"), h = h.replace(/\[cid2]/, "%3Bcid2%2CL{cid}M{cid}")
                }
                c = "//search.e.jd.com/searchDigitalBook?ajaxSearch=0&enc=utf-8&key={keyword}&page=1{additional}";
                break;
            case 6:
                j = "-1", c = "//music.jd.com/8_0_desc_0_0_1_15.html?key={keyword}"
        }
        if ("string" == typeof i && "" != i && "string" == typeof j) {
            var m = /^(?:[1-8])?([1-3])$/;
            j = "-1" == j ? "" : m.test(j) ? RegExp.$1 : "";
            var n = h.replace(/\{level}/, j);
            n = n.replace(/\{cid}/g, i), d += n
        }
        "string" == typeof k && "" != k && (d += "&ev=" + k), f = encodeURIComponent(f), sUrl = c.replace(/\{keyword}/, f), sUrl = sUrl.replace(/\{enc}/, "utf-8"), sUrl = sUrl.replace(/\{additional}/, d), ("undefined" == typeof b.isSubmitted || 0 == b.isSubmitted) && (setTimeout(function () {
            window.open(sUrl, "_blank"), b.isSubmitted = !1
        }, 10), b.isSubmitted = !0)
    }
}
function toFixUpLoc(a, b, c) {
    c.hide();
    "BackCompat" == document.compatMode ? document.body : document.documentElement;
    var e = b.offset().top;
    var f = parseInt(b.css("top"), 10);
    var g = a.offset().top;
    var h = $(document).scrollTop();
    if (!b.data("data-top")) {
        var i = parseInt(b.css("top"), 10);
        b.data("data-top", i)
    }
    var j = b.data("data-top");
    if (!c.data("data-top")) {
        var i = parseInt(c.css("top"), 10);
        c.data("data-top", i)
    }
    var k = c.data("data-top");
    if (h + 21 > e) {
        var l = c.offset().top;
        var m = parseInt(c.css("top"), 10);
        var n = g - e;
        var o = m - 23 - (l - g);
        b.css("top", f + n), c.css("top", Math.max(o, 0))
    } else b.css("top", j), c.css("top", k)
}
function toFixDownLoc(a, b) {
    b.hide();
    var c = "BackCompat" == document.compatMode ? document.body : document.documentElement;
    var d = c.clientHeight - 50;
    var e = a.offset().top;
    var f = parseInt(a.css("top"), 10);
    var g = a.outerHeight();
    var h = $(document).scrollTop();
    var i = d + h;
    var j = e + g;
    if (j - i > 0) {
        var k = f - (j - i) - 5;
        var l = j - i + 23;
        a.css("top", k), b.css("top", Math.max(Math.abs(k) - 15, l))
    }
}
function showUpBrowserTips() {
    var a = $.jCookie("browser-detect");
    if (!a && ($.browser.isIE6() || $.browser.isIE7())) {
        var b = '<div class="tipbox-browser tipbox-ie6"><div class="tipbox-inner"><span class="tipbox-close J-tipbox-close" clstag="clickcart|keycount|warn|cart_tishi_close">&times;</span><div class="ie6-tip"><i class="i-warn"></i><span class="text">\u60a8\u5f53\u524d\u4f7f\u7528\u7684\u6d4f\u89c8\u5668\u7c7b\u578b\u6216\u7248\u672c\u8fc7\u4f4e\uff0c\u53ef\u80fd\u5f71\u54cd\u60a8\u7684\u8d2d\u7269\u8f66\uff0c\u4e3a\u83b7\u5f97\u66f4\u597d\u7684\u8d2d\u7269\u4f53\u9a8c\uff0c\u5efa\u8bae\u4e0b\u8f7d\u5b89\u88c5\u6240\u63a8\u8350\u7684\u6d4f\u89c8\u5668\u3002</span><b></b></div><div class="good-browsers"><div class="top-title">\u5efa\u8bae\u4f7f\u7528\u6d4f\u89c8\u5668</div><ul class="browsers-list"><li><a href="http://rj.baidu.com/soft/detail/14744.html" clstag="clickcart|keycount|warn|cart_tishi_chrome" target="_blank"><i class="b-chrome"></i><span class="text">Chrome</span></a></li><li><a href="http://rj.baidu.com/soft/detail/11843.html" clstag="clickcart|keycount|warn|cart_tishi_huohu" target="_blank"><i class="b-firefox"></i><span class="text">Firefox</span></a></li></ul></div></div></div>';
        $("body").append(b);
        var c = $(".tipbox-ie6");
        c.fixable({
            x: "left",
            y: "bottom",
            xValue: 0,
            yValue: 0
        }), $("body").delegate(".J-tipbox-close", "click", function () {
            $.jCookie("browser-detect", 1, {expires: 90}), c.remove()
        })
    }
}
seajs.use(["jdf/1.0.0/ui/switchable/1.0.0/switchable"], function () {
    var b = '<div class="c-panel" id="walkBuy-products"><div class="goods-list-tab" style="width: 42px;"><a href="#none" class="s-item curr">&nbsp;</a><a href="#none" class="s-item">&nbsp;</a></div><div class="s-panel-main"><div class="goods-list s-panel"><ul><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|6"><a target="_blank" href="//item.jd.com/1798191.html" ><img width="160" height="160" src="//img11.360buyimg.com/n4/s160x160_jfs/t2689/10/4226899160/314552/e94acdda/57b27230N22c42f00.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u76ca\u8fbe\uff08Extra\uff09\u6728\u7cd6\u9187\u65e0\u7cd6\u53e3\u9999\u7cd6\u871c\u6843\u8292\u679c\u6df7\u5408\u547370\u7c9298g\u5355\u74f6\u88c5"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|7"><a target="_blank" href="//item.jd.com/1798191.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u76ca\u8fbe\uff08Extra\uff09\u6728\u7cd6\u9187\u65e0\u7cd6\u53e3\u9999\u7cd6\u871c\u6843\u8292\u679c\u6df7\u5408\u547370\u7c9298g\u5355\u74f6\u88c5</a></div><div class="p-price"><strong><em>\uffe5</em><i>13.90</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|8"><a href="#none" _pid="1798191" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|9"><a target="_blank" href="//item.jd.com/903427.html" ><img width="160" height="160" src="//img12.360buyimg.com/n1/s160x160_jfs/t499/77/224710997/118875/1ecba666/54575c66N403d1237.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u66fc\u59a5\u601d\u6e05\u52b2\u901f\u65e0\u7cd6\u53e3\u9999\u7cd6\u6e05\u65b0\u8584\u8377\u547356g\uff08\u65b0\u8001\u5305\u88c5\u968f\u673a\u53d1\u552e\uff09"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|10"><a target="_blank" href="//item.jd.com/903427.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u66fc\u59a5\u601d\u6e05\u52b2\u901f\u65e0\u7cd6\u53e3\u9999\u7cd6\u6e05\u65b0\u8584\u8377\u547356g\uff08\u65b0\u8001\u5305\u88c5\u968f\u673a\u53d1\u552e\uff09</a></div><div class="p-price"><strong><em>\uffe5</em><i>8.80</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|11"><a href="#none" _pid="903427" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|12"><a target="_blank" href="//item.jd.com/531065.html" ><img width="160" height="160" src="//img10.360buyimg.com/n4/s160x160_jfs/t3184/88/233644523/271559/21f538f5/57ac33d7Nc16466c3.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u7eff\u7bad\uff08DOUBLEMINT\uff09\u65e0\u7cd6\u8584\u8377\u7cd6\u539f\u5473\u8584\u8377\u547335\u7c9223.8g\u5355\u76d2\u91d1\u5c5e\u88c5"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|13"><a target="_blank" href="//item.jd.com/531065.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u7eff\u7bad\uff08DOUBLEMINT\uff09\u65e0\u7cd6\u8584\u8377\u7cd6\u539f\u5473\u8584\u8377\u547335\u7c9223.8g\u5355\u76d2\u91d1\u5c5e\u88c5</a></div><div class="p-price"><strong><em>\uffe5</em><i>7.90</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|14"><a href="#none" _pid="531065" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|15"><a target="_blank" href="//item.jd.com/736662.html" ><img width="160" height="160" src="//img12.360buyimg.com/n4/s160x160_jfs/t3481/346/2374567591/159192/994a1640/584e4949Na76fab78.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u597d\u65f6\u4e4b\u543bKisses\u725b\u5976\u5de7\u514b\u529b82g\uff08\u52a0\u91cf\u88c5\u4e0e\u6b63\u5e38\u88c5\u968f\u673a\u53d1\u552e\uff09"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|16"><a target="_blank" href="//item.jd.com/736662.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u597d\u65f6\u4e4b\u543bKisses\u725b\u5976\u5de7\u514b\u529b82g\uff08\u52a0\u91cf\u88c5\u4e0e\u6b63\u5e38\u88c5\u968f\u673a\u53d1\u552e\uff09</a></div><div class="p-price"><strong><em>\uffe5</em><i>12.80</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|17"><a href="#none" _pid="736662" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li></ul></div><div class="goods-list s-panel hide"><ul><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|18"><a target="_blank" href="//item.jd.com/3265177.html" ><img width="160" height="160" src="//img12.360buyimg.com/n4/s160x160_jfs/t3835/207/2268092525/279541/5ad566fb/5853ad4eN07e78c46.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u76ca\u8fbe\uff08Extra\uff09\u6728\u7cd6\u9187\u65e0\u7cd6\u53e3\u9999\u7cd6\u871c\u74dc\u8349\u839340\u7c9256g\u53cc\u74f6\u4fc3\u9500\u88c5"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|19"><a target="_blank" href="//item.jd.com/3265177.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u76ca\u8fbe\uff08Extra\uff09\u6728\u7cd6\u9187\u65e0\u7cd6\u53e3\u9999\u7cd6\u871c\u74dc\u8349\u839340\u7c9256g\u53cc\u74f6\u4fc3\u9500\u88c5</a></div><div class="p-price"><strong><em>\uffe5</em><i>17.50</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|20"><a href="#none" _pid="3265177" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|18"><a target="_blank" href="//item.jd.com/1158151.html" ><img width="160" height="160" src="//img11.360buyimg.com/n4/s160x160_jfs/t3490/310/1645784436/184882/6445dca/582ebdc4N89dd58d7.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u4e0d\u4e8c\u5bb6\u68d2\u68d2\u7cd6\uff08\u871c\u6843\u5473+\u8461\u8404\u5473+\u54c8\u5bc6\u74dc\u5473+\u9999\u6a59\u5473\uff09125g"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|19"><a target="_blank" href="//item.jd.com/1158151.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u4e0d\u4e8c\u5bb6\u68d2\u68d2\u7cd6\uff08\u871c\u6843\u5473+\u8461\u8404\u5473+\u54c8\u5bc6\u74dc\u5473+\u9999\u6a59\u5473\uff09125g</a></div><div class="p-price"><strong><em>\uffe5</em><i>12.50</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|20"><a href="#none" _pid="1158151" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|18"><a target="_blank" href="//item.jd.com/326463.html" ><img width="160" height="160" src="//img13.360buyimg.com/n4/s160x160_jfs/t298/6/558499924/144688/1681f00e/5417ba06N49fd5271.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u58eb\u529b\u67b6\u82b1\u751f\u5939\u5fc3\u5de7\u514b\u529b\u5206\u4eab\u88c5 \u7cd6\u679c\u5de7\u514b\u529b 240g"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|19"><a target="_blank" href="//item.jd.com/326463.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u58eb\u529b\u67b6\u82b1\u751f\u5939\u5fc3\u5de7\u514b\u529b\u5206\u4eab\u88c5 \u7cd6\u679c\u5de7\u514b\u529b 240g</a></div><div class="p-price"><strong><em>\uffe5</em><i>18.00</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|20"><a href="#none" _pid="326463" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li><li><div class="item"><div class="p-img" clstag="pageclick|keycount|cart_201610202|18"><a target="_blank" href="//item.jd.com/1083784.html" ><img width="160" height="160" src="//img14.360buyimg.com/n4/s160x160_g14/M09/1B/0B/rBEhVlMyLecIAAAAAAMljyTfjY0AAK1QQGW01YAAyWn717.jpg" alt="\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u963f\u5c14\u5351\u65af\u7cbe\u9009\u591a\u79cd\u53e3\u5473\u786c\u7cd6\u68d2\u68d2\u7cd6200g"></a></div><div class="p-name" clstag="pageclick|keycount|cart_201610202|19"><a target="_blank" href="//item.jd.com/1083784.html" >\u3010\u4eac\u4e1c\u8d85\u5e02\u3011\u963f\u5c14\u5351\u65af\u7cbe\u9009\u591a\u79cd\u53e3\u5473\u786c\u7cd6\u68d2\u68d2\u7cd6200g</a></div><div class="p-price"><strong><em>\uffe5</em><i>17.50</i></strong></div><div class="p-btn" clstag="pageclick|keycount|cart_201610202|20"><a href="#none" _pid="1083784" class="btn-append"><b></b>\u52a0\u5165\u8d2d\u7269\u8f66</a></div></div></li></ul></div></div><div class="c-page" ><a href="javascript:void(0)" class="c-prev">&lt;</a><a href="javascript:void(0)" class="c-next">&gt;</a></div></div>';
    $("#guess-products").after(b);
    var c = '<a href="#none" class="c-item curr" clstag="pageclick|keycount|cart_201610202|21">\u968f\u624b\u8d2d</a>';
    $(".c-item").eq(0).after(c);
    var d = "J_1798191,J_903427,J_531065,J_736662,J_3265177,J_1158151,J_326463,J_1083784";
    $.ajax({
        url: "//p.3.cn/prices/mgets?skuIds=" + d + "&area=&type=1&source=cartfe",
        type: "GET",
        dataType: "jsonp",
        scriptCharset: "utf-8",
        success: function (a) {
            a && 8 == a.length && $("#walkBuy-products").find(".p-price i").each(function (b) {
                a[b].p < 0 ? $(this).parent().html("\u6682\u65e0\u62a5\u4ef7") : $(this).html(a[b].p)
            })
        },
        error: function () {
        }
    }), $("#c-tabs-new .c-panel").switchable({
        type: "focus",
        navItem: "s-item",
        navSelectedClass: "curr",
        contentClass: "s-panel-main",
        mainClass: "s-panel",
        prevClass: "c-prev",
        nextClass: "c-next",
        hasPage: !0
    }), $(".mc", $("#c-tabs-new")).hover(function () {
        $(".c-page", $(this)).show()
    }, function () {
        $(".c-page", $(this)).hide()
    }), $("#c-tabs-new").switchable({
        type: "focus",
        navItem: "c-item",
        navSelectedClass: "curr",
        contentClass: "c-panel-main",
        mainClass: "c-panel",
        autoPlay: !1,
        callback: function (a) {
            if ("undefined" != typeof log)switch (a) {
                case 0:
                    log("newcart", "clickcart", "cart_xiHuanIn");
                    break;
                case 1:
                    log("pageclick|keycount|cart_201610202|21");
                    break;
                case 2:
                    log("newcart", "clickcart", "cart_guanZhuIn");
                    break;
                case 3:
                    log("newcart", "clickcart", "cart_collectIn")
            }
        }
    })
});