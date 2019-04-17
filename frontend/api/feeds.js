const Feeds = [
  {
    id: '7',
    manager: '김용국',
    staff: ['김태양', '김용국'],
    status: '긴급',
    title: '',
    memo: '일반사면을 명하려면 국회의 동의를 얻어야 한다.'
  },
  {
    id: '6',
    manager: '김용국',
    staff: ['김태양', '김용국'],
    status: '긴급',
    title: '',
    memo: '일반사면을 명하려면 국회의 동의를 얻어야 한다.'
  },
  {
    id: '5',
    manager: '김용국',
    staff: ['김태양', '김용국'],
    status: '긴급',
    title: '',
    memo: '일반사면을 명하려면 국회의 동의를 얻어야 한다.'
  },
  {
    id: '4',
    manager: '김용국',
    staff: ['kimyongkuk'],
    status: '긴급',
    title: '일반사면을 명하려면 국회의 동의를 얻어야 한다.',
    memo: '대통령이 임시회의 집회를 요구할 때에는 기간과 집회요구의 이유를 명시하여야 한다.'
  },
  {
    id: '3',
    manager: '김용국',
    staff: ['김용국'],
    status: '긴급',
    title: '',
    memo: '대통령은 제3항과 제4항의 사유를 지체없이 공포하여야 한다.'
  },
  {
    id: '2',
    manager: '김용국',
    staff: ['김용국'],
    status: '긴급',
    title: '',
    memo: '국가는 농수산물의 수급균형과 유통구조의 개선에 노력하여 가격안정을 도모함으로써 농·어민의 이익을 보호한다.'
  },
  {
    id: '1',
    manager: '김용국',
    staff: ['김용국'],
    status: '긴급',
    title: '',
    memo: '국회는 의원의 자격을 심사하며, 의원을 징계할 수 있다. 대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나온다.'
  }
]

const getFeeds = (limit) => {
  return (limit) ? Feeds.slice(0, limit) : Feeds
}

export {
  Feeds,
  getFeeds
}
