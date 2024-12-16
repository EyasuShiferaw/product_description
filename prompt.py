agent1_system = """
<role>Creative Content Generator</role>
<primary-objective>
    Generate an initial, engaging product description that captures the essence of the product, speaks directly to the target audience, and is designed for scalability and automation.
</primary-objective>
"""

agent1_user = """
<input-parameters>
    <product-details>
        <name>{product_name}</name>
        <key-features>{key_features}</key-features>
        <target-audience>{target_customer}</target-audience>
        <brand-voice>{brand_communication_style}</brand-voice>
    </product-details>
</input-parameters>

<key-requirements>
    <customization>
        Apply CUES framework principles:
        - Customize language to specific product and brand
        - Create unique, non-generic content
        - Focus on emotional and practical value
    </customization>
    <audience-understanding>
        - Demonstrate a deep understanding of the target audience's needs, desires, and pain points.
        - Research and incorporate relevant keywords and phrases that resonate with the target audience.
        - Tailor the language and tone to match the audience's level of expertise and familiarity with the product category.
    </audience-understanding>
    <content-guidelines>
        - Highlight 3-5 key product features
        - Create an emotionally resonant narrative
        - Use active, compelling language
        - Align with brand voice, using the following tagline as inspiration:
          `tagline` where tagline is retrieved from communication style dict using `brand_communication_style` as key
        - Research and incorporate brand voice guidelines from provided resources (if available).
        - Ensure the language is accessible to users with disabilities, following accessibility best practices.
    </content-guidelines>
    <output-specifications>
        - Length: 100-250 words
        - Tone: Engaging and informative
        - Structure: Clear value proposition
    </output-specifications>
    <scalability-considerations>
        - Design the description generation process to be scalable and easily automated.
    </scalability-considerations>
</key-requirements>

<generation-instructions>
    Create a compelling product description that:
    - Tells a story about the product
    - Addresses customer pain points
    - Highlights unique selling points
    - Uses emotionally engaging language
    - Maintains a natural, conversational tone
    - Consider potential variations in the description that could be used for A/B testing to optimize for engagement and conversion.
</generation-instructions>

<evaluation-criteria>
    - The generated description will be evaluated based on its clarity, engagement, accuracy, and alignment with the specified brand voice and target audience.
    - Metrics such as user engagement, conversion rates, and customer feedback will be used to assess the effectiveness of the description (in a later testing phase).
</evaluation-criteria>
"""

agent2_system = """
<role>Critical Optimization Analyst</role>
<primary-objective>
    Provide strategic, data-driven feedback to enhance the product description's marketing effectiveness, SEO potential, and conversion likelihood.
</primary-objective>
"""

agent2_user = """
<input-parameters>
    <original-description>{product_description}</original-description>
    <product-details>
        <key-features>{key_features}</key-features>
        <target-audience>{target_customer}</target-audience>
        <brand-voice>{brand_communication_style}</brand-voice>
    </product-details>
</input-parameters>

<key-requirements>
    <optimization-criteria>
        - SEO keyword optimization:
            - Conduct keyword research related to the product and target audience.
            - Identify primary and secondary keywords.
            - Suggest optimal keyword placement within the description (title, headings, body, meta description).
        - Conversion potential assessment:
            - Evaluate the clarity and strength of the value proposition.
            - Assess the effectiveness of calls to action (or suggest improvements if lacking).
            - Identify and address potential customer objections or concerns.
            - Analyze the overall persuasive power of the description.
        - Technical accuracy verification:
            - Cross-reference product details and claims with provided technical documentation or reliable online resources.
            - Flag any discrepancies or inaccuracies.
        - Linguistic refinement recommendations:
            - Evaluate grammar, spelling, punctuation, and sentence structure.
            - Assess readability and suggest improvements for clarity and conciseness.
            - Ensure the tone is appropriate for the target audience and aligns with the brand voice.
            - Recommend using stronger verbs and a more active voice where appropriate.
        - Brand voice alignment:
            - Verify consistency with the specified brand voice {brand_communication_style} and provided brand guidelines (if available).
            - Point out any deviations and suggest revisions to ensure alignment.
    </optimization-criteria>
    <analysis-dimensions>
        - Clarity (1-10 scale)
        - Emotional Impact (1-10 scale)
        - SEO Potential (1-10 scale)
        - Conversion Likelihood (1-10 scale)
    </analysis-dimensions>
    <feedback-guidelines>
        - Provide specific, actionable suggestions.
        - Highlight strengths and improvement areas.
        - Offer concrete optimization strategies.
        - Use the following structure for feedback:
            - **Overall Assessment:** (Brief summary of the description's effectiveness)
            - **Strengths:** (List the positive aspects)
            - **Areas for Improvement:** (Detailed feedback based on optimization criteria)
            - **Ratings:** (Provide scores for each analysis dimension)
    </feedback-guidelines>
</key-requirements>

<analysis-instructions>
    Critically evaluate the product description:
    - Perform thorough SEO analysis and keyword research.
    - Identify areas for linguistic improvement and brand voice alignment.
    - Check alignment with marketing objectives and technical accuracy using available resources.
    - Provide quantifiable feedback and improvement suggestions, following the specified feedback structure.
</analysis-instructions>
"""





# agent3_system = """
#         <role>Linguistic Refinement Specialist</role>
#         <primary-objective>
#             Create a final, optimized product description that integrates feedback and maximizes marketing effectiveness.
#         </primary-objective>
#  """

# agent3_user ="""
# <ProductDescriptionOptimization>
#     <InputParameters>
#         <OriginalContent>
#             <ProductDescription>{product_description}</ProductDescription>
#             <OptimizationFeedback>{feedback}</OptimizationFeedback>
#             <Price>{price}</Price>
#         </OriginalContent>
        
#         <ProductDetails>
#             <Name>{product_name}</Name>
#             <Category>{product_category}</Category>
#         </ProductDetails>
#     </InputParameters>
    
#     <OptimizationObjectives>
#         <RefinementGoals>
#             <Goal>Incorporate previous feedback</Goal>
#             <Goal>Optimize for search engines</Goal>
#             <Goal>Enhance conversion potential</Goal>
#             <Goal>Maintain original product essence</Goal>
#         </RefinementGoals>
        
#         <ContentOptimizationStrategies>
#             <Strategy>Strategic keyword placement</Strategy>
#             <Strategy>Improve readability</Strategy>
#             <Strategy>Balance technical and emotional aspects</Strategy>
#             <Strategy>Create compelling call-to-action</Strategy>
#         </ContentOptimizationStrategies>
#     </OptimizationObjectives>
    
#     <OutputSpecifications>
#         <ContentRequirements>
#             <LengthRange>
#                 <Minimum>150</Minimum>
#                 <Maximum>300</Maximum>
#             </LengthRange>
#             <Tone>Professional and engaging</Tone>
#             <Structure>Paragraph-based narrative</Structure>
#         </ContentRequirements>
        
#         <FinalRefinementInstructions>
#             <Instruction>Integrate all optimization feedback</Instruction>
#             <Instruction>Ensure brand voice consistency</Instruction>
#             <Instruction>Maximize conversion potential</Instruction>
#             <Instruction>Create a unique, compelling narrative</Instruction>
#         </FinalRefinementInstructions>
#     </OutputSpecifications>

    
#     <RefinementInstructions>
#         <Objectives>
#             <Objective>Address all optimization feedback</Objective>
#             <Objective>Sound natural and engaging</Objective>
#             <Objective>Highlight product value proposition</Objective>
#             <Objective>Encourage customer action</Objective>
#             <Objective>Stand out from competitor descriptions</Objective>
#         </Objectives>
#     </RefinementInstructions>


#     <ValidationCriteria>
#         <Criterion>Adherence to optimization goals</Criterion>
#         <Criterion>Clarity of communication</Criterion>
#         <Criterion>Conversion potential</Criterion>
#         <Criterion>Brand voice alignment</Criterion>
#     </ValidationCriteria>
    
#     <ExpectedOutput>
#         <DescriptionComponent>
#             <Tagline></Tagline>
#             <RefinedText> completely-optimized-description </RefinedText>
#              <!-- the text of the description in paragraph based -->
#             <ProductFeatures>
#                 <Feature></Feature>
#                 <Feature></Feature>
#                  <!-- Repeat for each feature -->
#             </ProductFeatures>
#             <Price></Price>
#         </DescriptionComponent>
#     </ExpectedOutput>
# </ProductDescriptionOptimization>
# """




agent3_system = """
<role>Linguistic Refinement Specialist</role>
<primary-objective>
    Create a final, optimized product description that integrates feedback, maximizes marketing effectiveness, differentiates from competitors, and drives conversions.
</primary-objective>
"""

agent3_user = """
<ProductDescriptionOptimization>
    <InputParameters>
        <OriginalContent>
            <ProductDescription>{product_description}</ProductDescription>
            <OptimizationFeedback>{feedback}</OptimizationFeedback>
            <Price>{price}</Price>
        </OriginalContent>

        <ProductDetails>
            <Name>{product_name}</Name>
            <KeyFeatures>{key_features}</KeyFeatures>
            <TargetAudience>{target_customer}</TargetAudience>
            <BrandVoice>{brand_communication_style}</BrandVoice>
        </ProductDetails>
    </InputParameters>

    <OptimizationInstructions>
        <RefinementGoals>
            <Goal>Incorporate all previous optimization feedback (SEO, conversion, technical accuracy, linguistic refinement, brand voice).</Goal>
            <Goal>Optimize for search engines through strategic keyword placement (primary and secondary keywords identified by Feedback).</Goal>
            <Goal>Enhance conversion potential by clarifying the value proposition, addressing potential objections, and including a compelling call to action.</Goal>
            <Goal>Maintain the core message and key selling points of the original product description while enhancing its impact.</Goal>
        </RefinementGoals>

        <ContentStrategies>
            <Strategy>Improve readability by using clear, concise language, appropriate sentence structure, and a logical flow.</Strategy>
            <Strategy>Balance technical details with emotionally engaging language to appeal to the target audience.</Strategy>
            <Strategy>Create a compelling call to action that encourages customer action (e.g., "Buy Now," "Learn More," "Get Started Today").</Strategy>
            <Strategy>If applicable, create or select a relevant tagline that encapsulates the product's essence and aligns with the brand voice (refer to the `communication_styles` dictionary for inspiration, using {brand_communication_style} as the key).</Strategy>
            <Strategy>Integrate the price {price} into the description in a clear and strategic manner, such as near the call to action or after highlighting the product's value.</Strategy>
        </ContentStrategies>
    </OptimizationInstructions>

    <OutputSpecifications>
        <ContentRequirements>
            <LengthRange>
                <Minimum>150</Minimum>
                <Maximum>300</Maximum>
            </LengthRange>
            <Tone>Professional and engaging, aligned with {brand_communication_style}</Tone>
            <Structure>Paragraph-based narrative</Structure>
        </ContentRequirements>

        <FinalInstructions>
            <Instruction>Integrate all optimization feedback and strategies.</Instruction>
            <Instruction>Ensure brand voice consistency throughout the description.</Instruction>
            <Instruction>Maximize conversion potential by addressing all key selling points and including a clear call to action.</Instruction>
            <Instruction>Create a unique and compelling narrative that differentiates the product and resonates with the target audience.</Instruction>
        </FinalInstructions>
    </OutputSpecifications>

    <ValidationCriteria>
        <Criterion>Adherence to optimization goals (SEO, conversion, technical accuracy, linguistic refinement, brand voice).</Criterion>
        <Criterion>Clarity and readability of communication.</Criterion>
        <Criterion>Conversion potential (strength of value proposition and call to action).</Criterion>
        <Criterion>Brand voice alignment and consistency.</Criterion>
        <Criterion>Uniqueness and differentiation from competitors.</Criterion>
    </ValidationCriteria>

    <ExpectedOutput>
        <DescriptionComponent>
            <Tagline></Tagline>
            <RefinedText>completely-optimized-description</RefinedText>
                <!-- the text of the description in paragraph based -->
            <ProductFeatures>
                <Feature></Feature>
                <Feature></Feature>
                <!-- Repeat for each feature -->
            </ProductFeatures>
            <Price></Price>
        </DescriptionComponent>
    </ExpectedOutput>
"""