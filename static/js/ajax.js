const productionCodeInput = document.getElementById('production_code')
const productCodeDisplay = document.getElementById('product_code')

productionCodeInput.addEventListener('change', e=>{
    //console.log('change')
    console.log(e.target.value)
    const inputData = e.target.value

    $.ajax({
        type: 'GET',
        url: `/production-code-json/${inputData}/`,
        success: function(response){
            console.log(response.data)
            const modelsData = response.data
            if ($.isEmptyObject(response.data)) {
                $("#product_code").val("Không tìm thấy mã sản phẩm")
            } else {
                modelsData.map(item=>{
                    $("#product_code").val(item.product_code)
                })
            }
        },
        error: function(error){
            console.log(error)
        }
    })
})


// $.ajax({
//     type: 'GET',
//     url: '/production-code-json/',
//     success: function(response){
//         console.log(response.data)
//         const productionCodeData = response.data
//         productionCodeData.map(item=>{
//             const option = document.createElement('input')
//             option.textContent = item.name
//             option.setAttribute('class', 'item')
//             option.setAttribute('data-value', item.name)
//             productionCodeDataBox
//         })
//     },
//     error: function(error){
//         console.log(error)
//     }
// })