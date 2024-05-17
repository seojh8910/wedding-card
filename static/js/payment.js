var today = new Date();
var hours = today.getHours(); // 시
var minutes = today.getMinutes();  // 분
var seconds = today.getSeconds();  // 초
var milliseconds = today.getMilliseconds();
var makeMerchantUid = hours + minutes + seconds + milliseconds;

function request_pay(name, email, username) {
    let IMP = window.IMP;
    let amount = {'모바일청첩장': 1000}
    IMP.init("imp81708134");
    IMP.request_pay({
        pg: 'kcp',
        pay_method: 'card',
        merchant_uid: "IMP" + makeMerchantUid,
        name: name,
        amount: amount[name],
        buyer_email: email,
        buyer_name: username,
    }, function (rsp) {
        pay_save(rsp)
    });
}

function pay_save(rsp) {
    $.ajax({
        url: "/payments/save/",
        type: "POST",
        data: {...rsp,},
        success: function (data) {
            if (data.status == 'saved')
                alert('저장');
            else
                alert('실패');
        }
    });
}
