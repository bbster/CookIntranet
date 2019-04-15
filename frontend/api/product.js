const Product = [
  {
    id: '1',
    name: '30박스올냉장 WSM-830R-3D',
    price: '840,000',
    barcode: '',
    memo: '일반사면을 명하려면 국회의 동의를 얻어야 한다. 대통령·국무총리·국무위원·행정각부의 장·헌법재판소 재판관·법관·중앙선거관리위원회 위원·감사원장·감사위원 기타 법률이 정한 공무원이 그 직무집행에 있어서 헌법이나 법률을 위배한 때에는 국회는 탄핵의 소추를 의결할 수 있다.'
  }
]
const getProduct = (limit) => {
  return (limit) ? Product.slice(0, limit) : Product
}
export {
  Product,
  getProduct
}
