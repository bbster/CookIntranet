const Feeds = [
  {
    id: '7',
    manager: '김용국',
    staff: ['김태양', '김용국'],
    status: '긴급',
    title: '모든 국민은 종교의 자유를 가진다. 국가는 건전한 소비행위를 계도하고 생산품의 품질향상을 촉구하기 위한 소비자보호운동을 법률이 정하는 바에 의하여 보장한다.',
    memo: '모든 국민은 그 보호하는 자녀에게 적어도 초등교육과 법률이 정하는 교육을 받게 할 의무를 진다. 피고인의 자백이 고문·폭행·협박·구속의 부당한 장기화 또는 기망 기타의 방법에 의하여 자의로 진술된 것이 아니라고 인정될 때 또는 정식재판에 있어서 피고인의 자백이 그에게 불리한 유일한 증거일 때에는 이를 유죄의 증거로 삼거나 이를 이유로 처벌할 수 없다.    모든 국민은 근로의 권리를 가진다. 국가는 사회적·경제적 방법으로 근로자의 고용의 증진과 적정임금의 보장에 노력하여야 하며, 법률이 정하는 바에 의하여 최저임금제를 시행하여야 한다.'
  },
  {
    id: '6',
    manager: '김용국',
    staff: ['김태양', '김용국'],
    status: '중요',
    title: '일반사면을 명하려면 국회의 동의를 얻어야 한다.',
    memo: '각급 선거관리위원회는 선거인명부의 작성등 선거사무와 국민투표사무에 관하여 관계 행정기관에 필요한 지시를 할 수 있다.'
  },
  {
    id: '5',
    manager: '김용국',
    staff: ['김태양', '김용국'],
    status: '긴급',
    title: '국정의 중요한 사항에 관한 대통령의 자문에 응하기 위하여 국가원로로 구성되는 국가원로자문회의를 둘 수 있다.',
    memo: '국토와 자원은 국가의 보호를 받으며, 국가는 그 균형있는 개발과 이용을 위하여 필요한 계획을 수립한다. 저작자·발명가·과학기술자와 예술가의 권리는 법률로써 보호한다.    국회나 그 위원회의 요구가 있을 때에는 국무총리·국무위원 또는 정부위원은 출석·답변하여야 하며, 국무총리 또는 국무위원이 출석요구를 받은 때에는 국무위원 또는 정부위원으로 하여금 출석·답변하게 할 수 있다.'
  },
  {
    id: '4',
    manager: '김용국',
    staff: ['kimyongkuk'],
    status: '보통',
    title: '일반사면을 명하려면 국회의 동의를 얻어야 한다.',
    memo: '대통령이 임시회의 집회를 요구할 때에는 기간과 집회요구의 이유를 명시하여야 한다.'
  },
  {
    id: '3',
    manager: '김용국',
    staff: ['김용국'],
    status: '긴급',
    title: '공무원인 근로자는 법률이 정하는 자에 한하여 단결권·단체교섭권 및 단체행동권을 가진다.',
    memo: '대통령은 제3항과 제4항의 사유를 지체없이 공포하여야 한다.'
  },
  {
    id: '2',
    manager: '김용국',
    staff: ['김용국'],
    status: '중요',
    title: '',
    memo: '국가는 농수산물의 수급균형과 유통구조의 개선에 노력하여 가격안정을 도모함으로써 농·어민의 이익을 보호한다.'
  },
  {
    id: '1',
    manager: '김용국',
    staff: ['김용국'],
    status: '긴급',
    title: '모든 국민은 헌법과 법률이 정한 법관에 의하여 법률에 의한 재판을 받을 권리를 가진다.',
    memo: '국회는 의원의 자격을 심사하며, 의원을 징계할 수 있다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.'
  }
]

/**
 * Feeds Create Function
 * @param
 */
const createFeeds = async function () {
  const data = await this.$axios.$get('feeds/create')
  return { data }
}
/**
 * Feeds GetList Function
 * @param
 */
const getFeeds = (limit) => {
  return (limit) ? Feeds.slice(0, limit) : Feeds
}
/**
 * Feeds Update Function
 * @param
 */
const updateFeeds = async function () {
  const data = await this.$axios.$get('feeds/update')
  return { data }
}
/**
 * Feeds Delete Function
 * @param
 */
const deleteFeeds = async function () {
  const data = await this.$axios.$get('feeds/delete')
  return { data }
}
/**
 * Feeds ReadDetail Function
 * @param
 */
const detailFeeds = async function () {
  const data = await this.$axios.$get('feeds/detail')
  return { data }
}
export {
  Feeds,
  createFeeds,
  getFeeds,
  updateFeeds,
  deleteFeeds,
  detailFeeds
}
