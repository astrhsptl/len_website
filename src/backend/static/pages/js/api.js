let serverDomain = "http://127.0.0.1:8000/";

const apiMap = {
    productCreate: serverDomain + "api/v1/docs/product/create/",
};

async function createNewProduct(event, id) {
    event.preventDefault();

    axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
    axios.defaults.xsrfCookieName = "csrftoken";
    
    let formData = new FormData(document.getElementsByClassName('active_form')[0]);
    
    formData.append("user", id);
    
    await axios.post(apiMap.productCreate, 
            formData, {
                headers: {
                    "Content-Type": "multipart/form-data",
                }}).then(res => res.data).catch(err => err);
                
    location.reload();
}