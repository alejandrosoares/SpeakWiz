import React from 'react';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/scrollbar';
import 'swiper/css/effect-cube';
import '../../assets/css/topic/TopicSlide.css';
import { Row, Col } from 'react-bootstrap';
import { EffectCube, Pagination } from 'swiper/modules';
import { Swiper, SwiperSlide } from 'swiper/react';
import getRandomColors from '../../utils/colors/getRandomColors';
import SoundBtn from '../buttons/SoundBtn';
import SlideCounter from './SildeCounter';

function TopicSlider({ slides }) {
  const totalSlides = slides.length;
  const colors = getRandomColors(totalSlides);

  const getSlideNumber = (index) => index + 1;
  return (
    <Swiper
      effect="cube"
      grabCursor
      cubeEffect={{
        shadow: true,
        slideShadows: true,
        shadowOffset: 20,
        shadowScale: 0.94,
      }}
      pagination
      modules={[EffectCube, Pagination]}
      className="TopicSlider"
    >
      {slides.map((slide, index) => (
        <SwiperSlide key={slide.id} className="TopicSlide" style={{ backgroundColor: colors[index] }}>
          <SlideCounter slideNumber={getSlideNumber(index)} total={totalSlides} />
          <Row>
            <Col xs={12}>
              <span>{slide.question}</span>
            </Col>
            <Col xs={12}>
              <SoundBtn text={slide.question} />
            </Col>
          </Row>
        </SwiperSlide>
      ))}
    </Swiper>
  );
}

export default TopicSlider;
